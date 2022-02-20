#================================================================
import sqlite3
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from datetime import datetime

import argparse
import re
import sys
import requests
#================================================================
# Start function: It will display the first conversation,
# you may name it something else but the message inside
# it will be sent to the user whenever they press ‘start’ at the very beginning.
updater = Updater(token="5103369968:AAGo6aNEUzeMpiEx9cKqqCLrK913uf32B00")
dispatcher = updater.dispatcher
def start(bot, update):
    payam = """
    🤖 خوش اومدی✨ \n
    خوشحال میشم حرف های دلت رو به سرمد و مونا برسونم.\n
    هرچی که دلت می‌خواد رو اینجا براشون بنویس 🙂
    """
    bot.sendMessage(chat_id=update.message.chat_id,text=payam)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
#================================================================
def getCm(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="فرستادم براشون. مطمئن باش از پیامت خوشحال میشن. از چنل لذت ببر مراقب خودتم باش❤️🫂")

    userInfo = update.message.chat
    userMessage = update.message.text
    print(userMessage)
    userId = userInfo['id']
    userName = userInfo['username']
    print(userInfo)

    bot.sendMessage(chat_id=1926913946, text="-------------------")
    bot.sendMessage(chat_id=1926913946, text="You have a new message Sarmad!\n\n {}".format(userMessage))
    bot.sendMessage(chat_id=1926913946, text="Message sender information:\n\n {}".format(str(userInfo)))
    bot.sendMessage(chat_id=1926913946, text="-------------------")
    bot.sendMessage(chat_id=88577648, text="-------------------")
    bot.sendMessage(chat_id=88577648, text="You have a new message Mona!\n\n {}".format(userMessage))
    bot.sendMessage(chat_id=88577648, text="Message sender information:\n\n {}".format(str(userInfo)))
    bot.sendMessage(chat_id=88577648, text="-------------------")

    cn = sqlite3.connect("zthdb.sqlite")
    cn.execute("PRAGMA ENCODING = 'utf8';")
    cn.text_factory = str
    cn.execute("CREATE TABLE IF NOT EXISTS user_comment(u_id MEDIUMINT, u_name VARCHAR(50), u_comment TEXT, u_time DATETIME);")
    cn.execute("INSERT INTO user_comment VALUES (?, ?, ?, ?,);", (userId, userName, userMessage, datetime.now()))
    cn.commit()
    cn.close()

cm_handler = MessageHandler(Filters.text, getCm)
dispatcher.add_handler(cm_handler)

updater.start_polling()
updater.idle()
updater.stop()
