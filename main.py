from telegram.ext import Updater, Dispatcher, CommandHandler,MessageHandler, Filters
from const import TOKEN
from functions import *

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, pashalki))
dispatcher.add_handler(MessageHandler(Filters.text, button))


updater.start_polling()