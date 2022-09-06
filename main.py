from settings import bot
from telebot import types
pay_pal = 0
pay_pal_x_2 = 'off'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Click for money')
    item2 = types.KeyboardButton('Magazine')
    item3 = types.KeyboardButton('Show balance')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Hi, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Click for money':
            if pay_pal_x_2 == 'on':
                pay_pal =+ 2
                bot.send_message(message.chat.id, 'added 2 money')
            else:
                pay_pal =+ 1
                bot.send_message(message.chat.id, 'added 1 money')

        elif message.text == 'Magazine':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Buy x 2 mutator for 1000 money')
            back = types.KeyboardButton('Back')
            markup.add(item1, back)

            bot.send_message(message.chat.id, 'Show balance'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Show balance':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Your balance')
            back = types.KeyboardButton('Back')
            markup.add(item1, back)

            bot.send_message(message.chat.id, 'Your money'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Back':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Click for money')
            item2 = types.KeyboardButton('Magazine')
            item3 = types.KeyboardButton('Show balance')

            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Back'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Buy x 2 mutator for 1000 money':
            if pay_pal > 100:
                pay_pal_x_2 = 'on'
                bot.send_message(message.chat.id, 'You bought x 2 bonus'.format(message.from_user), reply_markup=markup)
            elif:
                bot.send_message(message.chat.id, 'Dont much money'.format(message.from_user), reply_markup=markup)


bot.infinity_polling()
