from aiogram.utils import executor
import handlers
from create_bot import dp

async def start_up (_):
    print('Бот активирован')

handlers.registred_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=start_up)
