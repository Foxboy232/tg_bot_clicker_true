import telebot
from telebot import types
TOKEN = '5621251200:AAGXZHen5Hy3Q6Mh_Sfq5IXeDerpJDR5pBc'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Кликнуть')
    item2 = types.KeyboardButton('Магазин')
    item3 = types.KeyboardButton('Рандомное число')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


bot.polling(none_stop=True)
