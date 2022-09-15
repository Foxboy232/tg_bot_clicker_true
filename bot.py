from telebot import types
import random
from settings import bot
kiwi = 0
kiwi_boost = 0
charts = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
password = ''


def generate_password():
    global password
    for c in range(10):
        password =+ random.choice(chars)
    return password


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Кликнуть')
    item3 = types.KeyboardButton('Баланс')
    item4 = types.KeyboardButton('Рандомное число')
    item5 = types.KeyboardButton('Сгенерировать пароль (10 символов)')

    markup.add(item1, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    global kiwi, password
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
          bot.send_message(message.chat.id, 'Твоё число: ' + str(random.randint(0, 100)))
        elif message.text == 'Кликнуть':
            if kiwi_boost == 1:
                kiwi =+ 2
                bot.send_message(message.chat.id, '+2')
            else:
                kiwi =+ 1
                bot.send_message(message.chat.id, '+1')
        elif message.text == 'Баланс':
            bot.send_message(message.chat.id, f'у тебя: {kiwi}')
        elif message.text == 'Сгенерировать пароль (10 символов)':
            generate_password()


if __name__ == '__main__':
    bot.polling(none_stop=True)
