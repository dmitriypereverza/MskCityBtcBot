#!/usr/bin/python3
# -*- coding: utf-8 -*-
from enum import Enum

HEROKU_APP_NAME = 'warm-taiga-86371.herokuapp.com'
env='dev'
TELEGRAM_TOKEN='568880226:AAGX19mmh0jgT2BrQqz2johhzJiGPFc0k80'
db_file = "database.vdb"

BOT_STATES = {
    'start': {
        'transitions': [
            {
                'input': "^/start$",
                'next': 'select_action',
                'text': 'Что бы вы хотели?',
                'keyboard_btn': ['Купить bitcoin', 'Продать bitcoin', 'Связаться с менеджером']
            }
        ]
    },
    'select_action': {
        'transitions': [
            {
                'input': '^Купить bitcoin$',
                'next': 'end_state',
                'text': 'На какую сумму вы хотите купить?',
                'keyboard_btn': []
            },
            {
                'input': '^Продать bitcoin$',
                'next': 'end_state',
                'text': 'Какое кол-во bitcoin вы хотите продать?',
                'keyboard_btn': []
            },
            {
                'input': '^Связаться с менеджером$',
                'next': 'manager_connect',
                'text': 'Переадресовываю вас на менеджера! Задайте свой вопрос.',
                'keyboard_btn': []
            },
        ]
    },
    'manager_connect': {
        'transitions': [
            {
                'input': '.+',
                'next': 'end_state',
                'text': 'Ваш вопрос принят в обработку. Ожидайте...',
                'keyboard_btn': ['Хорошо', 'Спасибо']
            },
        ]
    },
    'end_state': {
        'transitions': [
            {
                'input': '.+',
                'next': 'start',
                'text': 'Спасибо за использование нашего бота',
                'keyboard_btn': []
            },
        ]
    }
}
class States(Enum):
    S_START = "start"
    S_SELECT_NAME = "select_action"
    S_END_NAME = "end_state"