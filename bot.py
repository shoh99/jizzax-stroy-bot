# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10Uo2mRK_lPE9iXmXqBhthmDPAj_AJ1QN
"""

# !pip install python-telegram-bot

import pandas as pd
import logging
import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# port
PORT = int(os.environ.get('PORT', 5000))
TOKEN = ''
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

reply_keyboard = [['Kontaktlar'], ['gisht palichka', 'vetnam silliq 6/6', 'madrid'], ['vetnam grand 6/6', 'rombek', 'marokash kubikcha'], ['gisht 6/6',
                                                                                                                                           'naqsh 30/30', 'marokash palichka'], ['30/30 grand', 'gisht 2', '20/20 grand 6/6'], ['30/30 10/30', '30/30 bolasi 16.5/12.5', 'fayz', '20/20 silliq 6/6']]
name_list = pd.read_csv('shapes_csv.csv')


def photo(update, context):
    choice = update.message.reply_text(
        "Yoqtirgan shaklingizni tanlang",
        reply_markup=telegram.ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=False))
    return choice


def reply(update, context):
    user_input = update.message.text

    update_name = name_list[name_list['BRUSCHATKA'] == user_input]
    for i in range(0, len(update_name)):
        if update_name.iloc[0][1] == 'Kontaktlar':
            url = update_name.iloc[i, 0]
            update.message.reply_text(url)
        else:
            url = update_name.iloc[i, 0]
            context.bot.send_photo(chat_id=update.message.chat_id, photo=url)


def error(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(
        TOKEN, use_context=True)

    dp = updater.dispatcher

    # dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('start', photo))
    dp.add_handler(MessageHandler(Filters.regex(
        '^(Kontaktlar|gisht palichka|vetnam silliq 6/6|madrid|vetnam grand 6/6|rombek|marokash kubikcha|gisht 6/6|naqsh 30/30|marokash palichka|30/30 grand|gisht 2|20/20 grand 6/6|30/30 10/30|30/30 bolasi 16.5/12.5|fayz|20/20 silliq 6/6)$'), reply))

    dp.add_error_handler(error)

    # start bot
    updater.start_webhook(listen='0.0.0.0',
                          port=int(PORT),
                          url_path=TOKEN)

    updater.bot.setWebhook('https://git.heroku.com/jizzax-stroy-bot/' + TOKEN)
    updater.idle()
https://git.heroku.com/jizzax-stroy-bot

if __name__ == '__main__':
    main()
