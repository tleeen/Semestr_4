from telegram.ext import Updater, MessageHandler, Filters
from kemsu_lab_bot import TG_TOKEN


def echo(update, context):
    update.message.reply_text("Я получил сообщение " + update.message.text)


def main():
    updater = Updater(TG_TOKEN, use_context=True)
    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)
    dp.add_handler(text_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
