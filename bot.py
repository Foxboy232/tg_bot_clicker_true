import telebot
from telebot import types
import random
TOKEN = '5758770402:AAHnkK0_xCAK1Pi9Eu6Q44z4HrgnOID3HsU'
bot = telebot.TeleBot(TOKEN)
kiwi = 0
kiwi_boost = 0


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Кликнуть')
    item2 = types.KeyboardButton('Магазин')
    item3 = types.KeyboardButton('Баланс')
    item4 = types.KeyboardButton('Рандомное число')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
          bot.send_message(message.chat.id, 'Твоё число: ' + str(random.randint(0, 100)))
        elif message.text == 'Магазин':
            item1 = types.KeyboardButton('Купить х 2 клики за 1000 кликов')
            back = types.KeyboardButton('Назад')
            markup.add(item1, back)
            bot.send_message(message.chat.id, 'выберите что вам надо')
        elif message.text == 'Кликнуть':
            if kiwi_boost == 1:
                kiwi =+ 2
                bot.send_message(message.chat.id, '+2')
            else:
                kiwi =+ 1
                bot.send_message(message.chat.id, '+1')
        elif message.text == 'Баланс':
            bot.send_message(message.chat.id, f'у тебя: {kiwi}')
        elif message.text == 'Купить х 2 клики за 1000 кликов':
            if kiwi > 1000 or kiwi == 1000:
                kiwi_boost == 1
            else:
                bot.send_message(message.chat.id, 'У вас меньше 1000 денег')
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Кликнуть')
            item2 = types.KeyboardButton('Магазин')
            item3 = types.KeyboardButton('Баланс')
            item4 = types.KeyboardButton('Рандомное число')
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'Назад'.format(message.from_user), reply_markup=markup)


bot.polling(none_stop=True)
