#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import re

import telebot
from flask import Flask, request

import utils
from DB import db
from app import config
from app.xml_config import XMLConifgBot

token = os.environ.get('TELEGRAM_TOKEN', config.TELEGRAM_TOKEN)
bot = telebot.TeleBot(token)
server = Flask(__name__)
botConfig = XMLConifgBot(config.xml_config_path)

@bot.message_handler(commands=['start'])
def message_handler(request):
    db.set_state(request.chat.id, config.States.S_START.value)
    main_message_handler(request)

@bot.message_handler()
def main_message_handler(request):
    transition = botConfig.getTransitionByText(db.get_current_state(request.chat.id), request.text)
    if transition:
        bot.send_message(request.chat.id, transition['text'], reply_markup=utils.generate_markup(transition['keyboard_btn'].split("||")))
        db.set_state(request.chat.id, transition['next'])

@server.route("/{}".format(token), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}/{}".format(config.HEROKU_APP_NAME, token))
    return "!", 200

if __name__ == '__main__':
    if config.env == 'dev':
        bot.polling(none_stop=True)
    else:
        server.run()