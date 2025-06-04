import telebot
from api import key


bot = telebot.TeleBot(key)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет!, {message.from_user.user_name}')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Привет, я бот <b>Жабьего императора Жмерлина</b>! Я создан с целью обучения моего господина', parse_mode='html')



bot.infinity_polling()

