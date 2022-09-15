from telebot import types
import random
from settings import bot


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Чтобы поиграть в камень  ножницы бумага пишите r, s, p (просто букву), чтобы узнать своё число пишите numb'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'numb':
            bot.send_message(message.chat.id, 'Твоё число: ' + str(random.randint(0, 100)))
        elif message.text == r:
            bot.pick == random.randint(0, 2)


bot.polling(none_stop=True)
