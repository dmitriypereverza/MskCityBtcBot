#!/usr/bin/python3
# -*- coding: utf-8 -*-
import telebot
import config
import utils
import cherrypy

bot = telebot.TeleBot(config.token)

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)


@bot.message_handler(commands=['start'])
def message_handler(request):
    answerButtons = ['Купить bitcoin', 'Продать bitcoin', 'Связаться с менеджером']
    bot.send_message(request.chat.id, 'Что бы вы хотели?', reply_markup=utils.generate_markup(answerButtons))
    return

@bot.message_handler()
def message_handler(request):
    if request.text in config.answers.keys():
        bot.send_message(request.chat.id, config.answers[request.text],
                         reply_markup=telebot.types.ReplyKeyboardHide())


# Снимаем вебхук перед повторной установкой (избавляет от некоторых проблем)
bot.remove_webhook()

# Ставим заново вебхук
bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH,
                certificate=open(config.WEBHOOK_SSL_CERT, 'r'))

bot.get_webhook_info()

cherrypy.config.update({
    'server.socket_host': config.WEBHOOK_LISTEN,
    'server.socket_port': config.WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': config.WEBHOOK_SSL_CERT,
    'server.ssl_private_key': config.WEBHOOK_SSL_PRIV
})


# Собственно, запуск!
cherrypy.quickstart(WebhookServer(), config.WEBHOOK_URL_PATH, {'/': {}})
