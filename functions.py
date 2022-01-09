import time
import markups as mrk
from telegram.constants import CHATACTION_TYPING

#from data import value
from data import value
from messages import *

def start(update, context):
    chat_id=update.message.chat_id
    name = start_text.format(update.message.chat.first_name)
    context.bot.send_message(chat_id=chat_id,
                             text=name, reply_markup=mrk.get_details())

def pashalki(update, context):
    text = update.message.text.lower()
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id=chat_id, action=CHATACTION_TYPING)
    time.sleep(1.0)

    if text == 'aziz':
        context.bot.send_message(chat_id = chat_id, text = 'Loves femdom')
    if text == 'donik':
        context.bot.send_message(chat_id = chat_id, text = 'Машина')
    if text == 'yon':
        context.bot.send_message(chat_id=chat_id, text="Yon is SaidAmalknon's fucking slave")
    if text == 'get information':
        context.bot.send_message(chat_id = chat_id, text = value)



def button(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id,
                             text='ok')



