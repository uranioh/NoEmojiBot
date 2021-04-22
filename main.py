# coding: utf-8
import logging
import re

from telegram.ext import Updater, MessageHandler, Filters

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def reader(update, context):
    if re.search("[^\x00-\x7F]+\ *(?:[^\x00-\x7F]| )*", update.message.text) and update.message.chat.type == "group":
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)


if __name__ == "__main__":
    updater = Updater(token='TOKEN', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reader))
    updater.start_polling()
    updater.idle()
