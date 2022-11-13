import os
from create_bot import bot
from aiogram import types
from pytube import YouTube


async def start(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, f'Привет {message.from_user.username}! Этот Бот предназначен для '
                                    f'скачивания видео из YouTube! Отправь мне ссылку 📹')


async def download_text(message: types.Message):
    url = message.text
    yt = YouTube(url)
    chat_id = message.chat.id
    if message.text.startswith == 'https://www.youtube.com/' or 'https://youtu.be/':
        await bot.send_message(chat_id, f"Начинаем загрузку {yt.title}", parse_mode='Markdown')
        await download_video(url, message, bot)
    else:
        await bot.send_message(chat_id, 'Вы ошиблись при вводе ссылки на видео, попробуйте еще раз! 🤨')


async def download_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f'{message.chat.id}/{message.chat.id}_{yt.title}', 'rb') as video:
        await bot.send_video(message.chat.id, video, caption='*Вот видео*', parse_mode='Markdown')
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')
