from telebot import TeleBot
from telebot import types
from settings import *

bot = TeleBot(dev_bot)
chat_id = -1001975865980

button = types.InlineKeyboardButton('Подробнее', url='t.me/bots_space')
example_button = types.InlineKeyboardButton('Посмотреть пример', url='https://vk.com/inburg')

keyboard = types.InlineKeyboardMarkup()
keyboard.add(button)
keyboard.add(example_button)


bot.edit_message_reply_markup(chat_id=chat_id, message_id=9, reply_markup=keyboard)
