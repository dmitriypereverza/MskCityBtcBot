#!/usr/bin/python3
# -*- coding: utf-8 -*-

WEBHOOK_HOST = '87.117.63.174'
WEBHOOK_PORT = 8443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
token = "568880226:AAGX19mmh0jgT2BrQqz2johhzJiGPFc0k80"
WEBHOOK_URL_PATH = "/%s/" % (token)

CHANNEL_NAME = '@omagat920'
message_chat_id = 433288067

answers = {
    'Купить bitcoin': 'На какую сумму вы хотите купить?',
    'Продать bitcoin': 'Какое кол-во bitcoin вы хотите продать?',
    'Связаться с менеджером': 'Переадресовываю вас на менеджера!'
}

