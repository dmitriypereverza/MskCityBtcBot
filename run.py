#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

import telebot
from flask import Flask, request

import config
import utils

bot = telebot.TeleBot(config.token)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def message_handler(request):
    answerButtons = ['Купить bitcoin', 'Продать bitcoin', 'Связаться с менеджером']
    bot.send_message(request.chat.id, 'Что бы вы хотели?', reply_markup=utils.generate_markup(answerButtons))
    return

@bot.message_handler()
def message_handler(request):
    if request.text in config.answers.keys():
        bot.send_message(request.chat.id, config.answers[request.text],
                         reply_markup=telebot.types.ReplyKeyboardRemove())

@server.route("/{}".format(config.token), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}/{}".format(config.HEROKU_APP_NAME, config.token))
    return "!", 200

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))