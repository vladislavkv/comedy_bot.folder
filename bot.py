import telebot
import requests
from settings import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])

def start(message):
    bot.send_message(message.chat.id,   'Enter message:')
    bot.register_next_step_handler(message, message_send)

def message_send(message):
    data = requests.get                                         \
    (API_URL, {'user_id'      : '-491',
               'message'      : 'message',
               'payload'      : '{"web_url":"'+message.text+'"}',
               'access_token' : ACCESS_TOKEN,
               'v'            : '5.85'                         })
    bot.send_message(message.chat.id,            'Successfully!')

bot.polling(none_stop = True)