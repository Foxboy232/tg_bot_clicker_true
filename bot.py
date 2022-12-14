from telebot import types
import random
from settings import bot
kiwi = 0
kiwi_boost = 0
charts = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*_+-='
password = ''


def generate_password():
    global password
    for c in range(10):
        password += random.choice(charts)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Орёл - решка')
    item2 = types.KeyboardButton('???')
    item3 = types.KeyboardButton('Кликнуть')
    item4 = types.KeyboardButton('Реклама')
    item5 = types.KeyboardButton('Количество кликов')
    item6 = types.KeyboardButton('Рандомное число')
    item7 = types.KeyboardButton('Сгенерировать пароль (10 символов)')
    item8 = types.KeyboardButton('Потревожить автора')

    markup.add(item3, item5, item4, item6, item8, item7, item1, item2)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    global kiwi, password
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
          bot.send_message(message.chat.id, 'Твоё число: ' + str(random.randint(0, 100)))
        elif message.text == 'Кликнуть':
            kiwi += 1
            bot.send_message(message.chat.id, '+1')
        elif message.text == 'Количество кликов':
            bot.send_message(message.chat.id, f'у бота: {kiwi} кликов')
        elif message.text == 'Сгенерировать пароль (10 символов)':
            generate_password()
            bot.send_message(message.chat.id, f'{password}')
            password = ''
        elif message.text == 'Реклама':
            rando = random.randint(0, 5)
            if rando == 0:
                bot.send_message(message.chat.id, 'Хеден шолдерс! Лучший шампунь от головы!')
            elif rando == 1:
                bot.send_message(message.chat.id, 'Корега 9 из 10 стоматологов рекомендуют эту зубную пасту')
            elif rando == 2:
                bot.send_message(message.chat.id, 'Джо Джо! Лучшее аниме века')
            elif rando == 3:
                bot.send_message(message.chat.id, 'Весь мир Джо Джо референс!')
            elif rando == 4:
                bot.send_message(message.chat.id, 'Капуста! 9 из 10 фермеров ставят лайк!')
            elif rando == 5:
                bot.send_message(message.chat.id, 'Кроссаут, это онлайн шутер где ты можешь собрать машину из говна')
        elif message.text == '???':
            bot.send_message(message.chat.id, '???')
        elif message.text == 'Орёл - решка':
            opel_reshka_choice = random.randint(0, 1)
            if opel_reshka_choice == 0:
                bot.send_message(message.chat.id, 'Вам выпал: ' + str('Орёл'))
            else:
                bot.send_message(message.chat.id, 'Вам выпала: ' + str('Решка'))
        elif message.text == 'Потревожить автора':
            bot.send_message(message.chat.id, 'Автор показывает код, не мешать!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
