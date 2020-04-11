# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters, BaseFilter
import config
import re
import random
import time
import qrcode
import os
import subprocess
import speech_recognition as sr
import urllib


# Load Config
TOKEN = config.Telegram['TOKEN']


# Setup Bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


# Main Bot Functions

# Commands 

# /start - Fist message, when user start bot
def start (update, context):
    update.effective_chat.send_message(text='Я бот, пожалуйста, поговори со мной!')

# /my_name - Send User Name
def send_user_name (update, context):
    full_name = update.effective_user.full_name
    update.effective_chat.send_message(text=f'Ваше имя: {full_name}')

# /my_photo - Send User Photo Avatar 
def send_user_photo (update, context):

    user_photos = update.effective_user.get_profile_photos()

    if user_photos.total_count > 0:
        # Send maximal aviable photo size
        update.effective_chat.send_photo(user_photos.photos[0][-1])

# /qr_code 'INFO' - Make and Send QR Code from INFO
def send_qr_code (update, context):

    # Check to INFO after /qr_code
    if len(context.args) > 0:
        information = ' '.join(context.args)
        qr_code_img = qrcode.make(information)

        qr_code_img.save("qr_code.jpg")
        file_qr_code = open("qr_code.jpg", "rb")

        update.effective_user.send_photo(photo=file_qr_code)
    else: 
        update.effective_user.send_message('/qr_code "Осутсвует информация"\nВведите информацию которую нужно преобразовать в QR код')

# Messages

# ...[?] - Send random Chance
def send_rand_chance (update, context):

    random.seed(random.seed(time.time()))
    chance = random.randint(0, 100)

    answers = [
        "Нет",
        "Скорее нет, чем да",
        "Скорее да, чем нет",
        "Да"
    ]

    if chance < 40:
        key = 0
    elif chance < 50:
        key = 1
    elif chance < 60:
        key = 2
    else:
        key = 3

    update.effective_chat.send_message(answers[key])

# Voice 

def wav2text (dest_filename, file_name):
    r = sr.Recognizer()
    message = sr.AudioFile(dest_filename)

    with message as source:
        audio = r.record(source)
    try:
        result = r.recognize_google(audio, language="ru-RU")
        os.remove(dest_filename)
        os.remove(file_name)
        return format(result)

    except sr.UnknownValueError:
        os.remove(dest_filename)
        os.remove(file_name)
        return 'Не удалось распознать текст'

def oga2wav (file_name):
    src_filename = file_name
    dest_filename = file_name + '.wav'
    process = subprocess.run(['ffmpeg', '-i', src_filename, dest_filename])

    return wav2text(dest_filename, file_name)

def oga2text (url, file_id):
    # Download .oga
    urllib.request.urlretrieve(url, file_id + '.oga')
    file_name = file_id + '.oga'

    return oga2wav(file_name)

# Send message from Voice.oga
def send_text_from_voice (update, context):
    
    audio = update.effective_message.voice.get_file()

    audio_PATH = audio['file_path']
    audio_FILE_ID = audio['file_id']
    
    message = oga2text(url=audio_PATH, file_id=audio_FILE_ID)
    update.effective_chat.send_message(text=message.capitalize())


# Handlers Obj
start_handler = CommandHandler ('start', start)
send_user_name_handler = CommandHandler ('my_name', send_user_name)
send_user_photot_handler = CommandHandler ('my_photo', send_user_photo)
send_qr_code_handler = CommandHandler ('qr_code', send_qr_code)
send_rand_chance_handler = MessageHandler (Filters.regex(r'\?'), send_rand_chance)
send_text_from_voice_handler = MessageHandler (Filters.voice, send_text_from_voice)

# Add Handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(send_user_name_handler)
dispatcher.add_handler(send_user_photot_handler)
dispatcher.add_handler(send_qr_code_handler)
dispatcher.add_handler(send_rand_chance_handler)
dispatcher.add_handler(send_text_from_voice_handler)


# Start Polling
updater.start_polling(poll_interval=5.0)
updater.idle()