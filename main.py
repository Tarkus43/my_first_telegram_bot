import telebot
import webbrowser
from telebot import types
# from api import key

key = '6886283736:AAEgEXByx3CM39IAOFe6mwNtqitWmypftMo'

bot = telebot.TeleBot(key)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    bot.send_message(message.chat.id,'Я украл твоё фото!!!', reply_markup=markup)

# commands //////////////////////////
@bot.message_handler(commands=['site'])
def website(message):
    webbrowser.open('https://www.google.com/')


@bot.message_handler(commands=['info'])
def info(message):
     bot.send_message(message.chat.id, message)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def help(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(types.InlineKeyboardButton('Мой гитхаб', url='https://github.com/Tarkus43'))
    
    bot.send_message(message.chat.id, 'Привет, я бот <b>Жабьего императора Жмерлина</b>! Я создан с целью обучения моего господина', parse_mode='html', reply_markup=markup )
# //////////////////////////////////


@bot.message_handler()
def reply(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'ПРИВИИИИТ💋✨💕❤️😍😊💕😍')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
       



bot.infinity_polling()

