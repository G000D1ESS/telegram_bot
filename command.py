# -*- coding: utf-8 -*-

""" Раздел отвечающий за все функции связанные с Command """

import qrcode

# /start - Первое сообщение, которое увидит пользователь
def start (update, context):
    update.effective_chat.send_message(text='Я бот, пожалуйста, поговори со мной!')

# /my_name - Отправить имя пользователя
def send_user_name (update, context):
    full_name = update.effective_user.full_name
    update.effective_chat.send_message(text=f'Ваше имя: {full_name}')

# /my_photo - Отправить Аватарку пользователя
def send_user_photo (update, context):

    user_photos = update.effective_user.get_profile_photos()

    if user_photos.total_count > 0:
        # Отправить фото в максимальном разрешении
        update.effective_chat.send_photo(user_photos.photos[0][-1])

# /qr_code 'INFO' - Отправить QR код с информацией "INFO"
def send_qr_code (update, context):

    # Проверить наличие информации
    if len(context.args) > 0:
        information = ' '.join(context.args)
        qr_code_img = qrcode.make(information)

        qr_code_img.save("qr_code.jpg")
        file_qr_code = open("qr_code.jpg", "rb")

        update.effective_user.send_photo(photo=file_qr_code)
    else: 
        update.effective_user.send_message('/qr_code "Осутсвует информация"\nВведите информацию которую нужно преобразовать в QR код')
