import telegram
from telegram.ext import *

mi_bot=telegram.Bot(token="1148167972:AAFP3Xa5ddl-bnZiXgyG_s9CSMNPvSLsJUM")
mi_bot_updater= Updater(mi_bot.token)

def start(bot,update, pass_chat_data=True):
    update.message.chat_id
    bot.sendMessage(chat_id=update.message.chat_id, text="Hola soy tu bot!")

start_handler=CommandHandler('start',start)
Dispatcher= mi_bot_updater.dispatcher
Dispatcher.add_handler(start_handler)
mi_bot_updater.start_polling()
mi_bot_updater.idle()

while True:
    pass
