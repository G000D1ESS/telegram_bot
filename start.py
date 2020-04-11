# -*- coding: utf-8 -*-

from bot_class import telegram_bot
import config

TOKEN = config.Telegram['TOKEN']

tg_bot = telegram_bot(TOKEN)
tg_bot.start()