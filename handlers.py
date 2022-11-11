from aiogram.dispatcher import Dispatcher
import commands

def registred_hendlers (dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])