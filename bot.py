# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler
import config
import qrcode 


# Load Config
TOKEN = config.Telegram['TOKEN']


# Setup Bot
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


# Main Bot Functions

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


# Handlers Obj
start_handler = CommandHandler('start', start)
send_user_name_handler = CommandHandler('my_name', send_user_name)
send_user_photot_handler = CommandHandler('my_photo', send_user_photo)
send_qr_code_handler = CommandHandler('qr_code', send_qr_code)


# Add Handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(send_user_name_handler)
dispatcher.add_handler(send_user_photot_handler)
dispatcher.add_handler(send_qr_code_handler)

# NEW INFO

# Start Polling
updater.start_polling(poll_interval=5.0)
updater.idle()