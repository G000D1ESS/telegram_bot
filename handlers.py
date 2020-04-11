# -*- coding: utf-8 -*-

""" Создание Хендлеров, Добавление в дипетчер """

from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import Filters, BaseFilter

import command
import message
import voice

### Создание обектов хенделеров ###

# Комманды 
start_handler = CommandHandler ('start', command.start)
send_user_name_handler = CommandHandler ('my_name', command.send_user_name)
send_user_photo_handler = CommandHandler ('my_photo', command.send_user_photo)
send_qr_code_handler = CommandHandler ('qr_code', command.send_qr_code)

# Сообщения
send_rand_chance_handler = MessageHandler (Filters.regex(r'\?'), message.send_rand_chance)

# Голосовые сообщения
send_text_from_voice_handler = MessageHandler (Filters.voice, voice.send_text_from_voice)

### ### ### ### ### ### ### ### ### ### 

# Список всех хендеров, не забудьте изменить после доавления нового
handlers_list = [

    # Комманды
    start_handler,
    send_user_name_handler,
    send_user_photo_handler,
    send_qr_code_handler,

    # Сообщения
    send_rand_chance_handler,

    # Голосовые сообщения
    send_text_from_voice_handler
]
