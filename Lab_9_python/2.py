from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from kemsu_lab_bot import TG_TOKEN
import datetime


def echo(update, context):
    update.message.reply_text("Я получил сообщение " + update.message.text)


def time(update, context):
    a = datetime.datetime.now()
    h = str(a.hour)
    m = str(a.minute)
    s = str(a.second)
    update.message.reply_text(h + ":" + m + ":" + s)


def date(update, context):
    a = datetime.datetime.now()
    y = str(a.year)
    m = str(a.month)
    d = str(a.day)
    update.message.reply_text(d + "/" + m + "/" + y)

def main():
    updater = Updater(TG_TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(CommandHandler("time", time))
    dp.add_handler(CommandHandler("date", date))
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
