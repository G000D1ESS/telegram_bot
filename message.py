# -*- coding: utf-8 -*-

""" Данный раздел отвечает за все Message функции """

import time
import random

# ...[?] - Отправить псведо-рандомный ответ на вопрос
def send_rand_chance (update, context):

    random.seed(random.seed(time.time()))
    chance = random.randint(0, 100)

    answers = ["Нет", "Скорее нет, чем да", "Скорее да, чем нет", "Да"]

    # 4 Варианта ответа => 40%, 10%, 10%, 40% 
    if chance < 40:
        key = 0
    elif chance < 50:
        key = 1
    elif chance < 60:
        key = 2
    else:
        key = 3

    update.effective_chat.send_message(answers[key])
