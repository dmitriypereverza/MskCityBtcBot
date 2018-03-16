#!/usr/bin/python3
# -*- coding: utf-8 -*-
import telebot

def generate_markup(answers):
    if not answers:
        return telebot.types.ReplyKeyboardRemove()
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in answers:
        markup.add(item)
    return markup
