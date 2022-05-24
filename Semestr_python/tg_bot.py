import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
from token_tg import TOKEN

bot = telebot.TeleBot(TOKEN)

a = 0


@bot.message_handler(commands=['start'])
def start(massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('На сегодня')
    item2 = types.KeyboardButton('На завтра')
    item3 = types.KeyboardButton('На неделю')
    item4 = types.KeyboardButton('Информация')

    markup.add(item1, item2, item3, item4)

    bot.send_message(massage.chat.id, 'Привет, {0.first_name}'.format(massage.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_massage(massage):
    global a
    if massage.chat.type == 'private':
        if massage.text == 'На сегодня':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('♈️ Овен')
            item2 = types.KeyboardButton('♉️ Телец')
            item3 = types.KeyboardButton('♊️ Близнецы')
            item4 = types.KeyboardButton('♋️ Рак')
            item5 = types.KeyboardButton('♌️ Лев')
            item6 = types.KeyboardButton('♍️ Дева')
            item7 = types.KeyboardButton('♎️ Весы')
            item8 = types.KeyboardButton('♏️ Скорпион')
            item9 = types.KeyboardButton('♐️ Стрелец')
            item10 = types.KeyboardButton('♑️ Козерог')
            item11 = types.KeyboardButton('♒️ Водолей')
            item12 = types.KeyboardButton('♓️ Рыбы')
            back = types.KeyboardButton('🔙 Назад')
            a = 1

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

            bot.send_message(massage.chat.id, 'На сегодня', reply_markup=markup)

        elif massage.text == 'На завтра':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('♈️ Овен')
            item2 = types.KeyboardButton('♉️ Телец')
            item3 = types.KeyboardButton('♊️ Близнецы')
            item4 = types.KeyboardButton('♋️ Рак')
            item5 = types.KeyboardButton('♌️ Лев')
            item6 = types.KeyboardButton('♍️ Дева')
            item7 = types.KeyboardButton('♎️ Весы')
            item8 = types.KeyboardButton('♏️ Скорпион')
            item9 = types.KeyboardButton('♐️ Стрелец')
            item10 = types.KeyboardButton('♑️ Козерог')
            item11 = types.KeyboardButton('♒️ Водолей')
            item12 = types.KeyboardButton('♓️ Рыбы')
            back = types.KeyboardButton('🔙 Назад')
            a = 2

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

            bot.send_message(massage.chat.id, 'На завтра', reply_markup=markup)

        elif massage.text == 'На неделю':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('♈️ Овен')
            item2 = types.KeyboardButton('♉️ Телец')
            item3 = types.KeyboardButton('♊️ Близнецы')
            item4 = types.KeyboardButton('♋️ Рак')
            item5 = types.KeyboardButton('♌️ Лев')
            item6 = types.KeyboardButton('♍️ Дева')
            item7 = types.KeyboardButton('♎️ Весы')
            item8 = types.KeyboardButton('♏️ Скорпион')
            item9 = types.KeyboardButton('♐️ Стрелец')
            item10 = types.KeyboardButton('♑️ Козерог')
            item11 = types.KeyboardButton('♒️ Водолей')
            item12 = types.KeyboardButton('♓️ Рыбы')
            back = types.KeyboardButton('🔙 Назад')
            a = 3

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, back)

            bot.send_message(massage.chat.id, 'На неделю', reply_markup=markup)

        elif massage.text == '🔙 Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('На сегодня')
            item2 = types.KeyboardButton('На завтра')
            item3 = types.KeyboardButton('На неделю')
            item4 = types.KeyboardButton('Информация')

            markup.add(item1, item2, item3, item4)

            bot.send_message(massage.chat.id, 'Назад', reply_markup=markup)

        elif massage.text == 'Информация':
            bot.send_message(massage.chat.id, 'Этот бот создан для того чтобы предсказать вашу судьбу на ближайшее '
                                              'будущее. При выборе одного из пунктов меню будут предложены знаки '
                                              'зодиака. Вы можете выбрать подходящий именно вам. Всегда можно '
                                              'вернуться назад, нажав соответствующую кнопку. Приятного пользования')

        elif massage.text == '♈️ Овен':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[0])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[0])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[0])

        elif massage.text == '♉️ Телец':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[1])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[1])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[1])

        elif massage.text == '♊️ Близнецы':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[2])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[2])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[2])

        elif massage.text == '♋️ Рак':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                print(clear_today[3])
                bot.send_message(massage.chat.id, clear_today[3])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[3])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[3])

        elif massage.text == '♌️ Лев':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[4])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[4])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[4])

        elif massage.text == '♍️ Дева':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[5])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[5])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[5])

        elif massage.text == '♎️ Весы':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[6])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[6])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[6])

        elif massage.text == '♏️ Скорпион':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[7])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[7])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[7])

        elif massage.text == '♐️ Стрелец':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[8])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[8])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[8])

        elif massage.text == '♑️ Козерог':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[9])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[9])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[9])

        elif massage.text == '♒️ Водолей':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[10])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[10])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[10])

        elif massage.text == '♓️ Рыбы':
            if a == 1:
                URL = 'https://74.ru/horoscope/daily/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                today = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_today = [i.text for i in today]
                bot.send_message(massage.chat.id, clear_today[11])
            elif a == 2:
                URL = 'https://74.ru/horoscope/tomorrow/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_tomorrow = [i.text for i in tomorrow]
                bot.send_message(massage.chat.id, clear_tomorrow[11])
            elif a == 3:
                URL = 'https://74.ru/horoscope/weekly/'
                r = requests.get(URL)
                soup = BeautifulSoup(r.text, 'html.parser')
                weak = soup.find_all('div', class_='_2j-zP _1ylC5')
                clear_weak = [i.text for i in weak]
                bot.send_message(massage.chat.id, clear_weak[11])


bot.polling(none_stop=True)
