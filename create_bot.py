from aiogram.bot import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token='5774076730:AAETxNKtPvFFk285caTvcf1HbCOpo3MxhMY')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
