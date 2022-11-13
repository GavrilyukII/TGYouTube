from aiogram.dispatcher import Dispatcher
import commands

def registred_handlers (dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.download_text)
    # dp.register_message_handler(commands.download_video)
