# -*- coding: utf-8 -*-

""" Раздел отвечающий за все функции связанные с Voice """

import speech_recognition as sr
import os
import subprocess
import urllib

# Преобразовать .wav в Текст
def wav2text (dest_filename, file_name):

    # Загрузка аудио-файла с сервера
    r = sr.Recognizer()
    message = sr.AudioFile(dest_filename)

    with message as source:
        audio = r.record(source)

        # Попытка распознания текста с помощью Гугла
        try:
            result = r.recognize_google(audio, language="ru-RU")
            os.remove(dest_filename)
            os.remove(file_name)
            return format(result)

        except sr.UnknownValueError:
            os.remove(dest_filename)
            os.remove(file_name)
            return 'Не удалось распознать текст'

# Преобразовать .oga в .wav
def oga2wav (file_name):
    src_filename = file_name
    dest_filename = file_name + '.wav'

    # На системе должен быть установлен Ffmpeg [ включен тихий режим ]
    process = subprocess.run(['ffmpeg','-loglevel', 'quiet', '-i', src_filename, dest_filename])

    return wav2text(dest_filename, file_name)

# Преобразовать .oga в Текст
def oga2text (url, file_id):

    # Скачать .oga с сервера Telegram
    urllib.request.urlretrieve(url, file_id + '.oga')
    file_name = file_id + '.oga'

    return oga2wav(file_name)

# Отправить текст голосового сообщения
def send_text_from_voice (update, context):
    
    audio = update.effective_message.voice.get_file()

    audio_PATH = audio['file_path']
    audio_FILE_ID = audio['file_id']
    
    message = oga2text(url=audio_PATH, file_id=audio_FILE_ID)
    update.effective_chat.send_message(text=message.capitalize())