import telebot
from telebot import types
import const
from geopy.distance import vincenty

bot = telebot.TeleBot(const.API_TOKEN)
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_catalog = types.KeyboardButton('Каталог')
btn_card = types.KeyboardButton('Корзина')
btn_order = types.KeyboardButton('Заказы')
btn_news = types.KeyboardButton('Новости')
btn_address = types.KeyboardButton('Адреса магазинов', request_location=True, )
btn_settings = types.KeyboardButton('Настройки')
markup_menu.add(btn_catalog, btn_card, btn_order, btn_news, btn_address, btn_settings)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, добро пожаловать в наш магазин", reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Каталог':
        bot.reply_to(message, '', reply_markup=markup_menu)
    elif message.text == 'Корзина':
        bot.reply_to(message, 'Купить лес и заблудиться в нём', reply_markup=markup_menu)
    elif message.text == 'Заказы':
        bot.reply_to(message, 'купи', reply_markup=markup_menu)
    else:
        bot.reply_to(message, message.text, reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True, content_types=['location'])
def shop_location(message):
    lon = message.location.longitude
    lat = message.location.latitude
    print('Широта {} Долгота {}'.format(lon, lat))


bot.infinity_polling()
