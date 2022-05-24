import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

TOKEN = '5299298158:AAGA_Yxq-GsFnMHsZzbmfGQ-XOQD3A_wJhA'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('На сегодня')
    item2 = types.KeyboardButton('На завтра')
    item3 = types.KeyboardButton('На неделю')
    item4 = types.KeyboardButton('Информация')

    markup.add(item1, item2, item3, item4)

    bot.send_message(massage.chat.id, 'Hello, {0.first_name}'.format(massage.from_user), reply_markup=markup)


# получение знака задиака
URL = 'https://74.ru/horoscope/daily/'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
zodiac = soup.find_all('h3', class_='kO5pM aTz6W')
clear_zodiac = [i.text for i in zodiac]
print(clear_zodiac[0])

# на сегодня
URL = 'https://74.ru/horoscope/daily/'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
today = soup.find_all('div', class_='_2j-zP _1ylC5')
clear_today = [i.text for i in today]
print(clear_today[0])

# на завтра
URL = 'https://74.ru/horoscope/tomorrow/'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
tomorrow = soup.find_all('div', class_='_2j-zP _1ylC5')
clear_tomorrow = [i.text for i in tomorrow]
print(clear_tomorrow[0])

# на неделю
URL = 'https://74.ru/horoscope/weekly/'
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
weak = soup.find_all('div', class_='_2j-zP _1ylC5')
clear_weak = [i.text for i in weak]
print(clear_weak[0])

bot.polling(none_stop=True)
