# -*- coding: utf-8 -*-

from telegram.ext import Updater
from handlers import handlers_list

class telegram_bot:

    """ Телеграмм бот с ограниченными функциями """ 
    
    # Инициализация телеграмм бота с помощью токена 
    def __init__(self, TOKEN):

        # Создание обьектов Телеграмм бота
        self.updater = Updater(token=TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # Добавление хендлеров в Диспетчер
        for handler in handlers_list:
            self.dispatcher.add_handler(handler)

    # Старт бота
    def start(self):
        self.updater.start_polling(poll_interval=5.0)
        self.updater.idle()
        