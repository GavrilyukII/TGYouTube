from aiogram.utils import executor
import handlers
from TGbot.main import on_startup
from create_bot import dp

async def start_up (_):
    print('Бот активирован')

handlers.registred_hendlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
