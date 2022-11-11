from create_bot import bot
from aiogram import types

async def start (message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.username}! Этот бот предназначен для '
                                                 f'скачивания видео из YouTube')
