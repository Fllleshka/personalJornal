# Библиотека для работы с Ботом
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove
# Импорт класса для текстовых сообщений
from dates.startcommands import textmessages

# Создаём роутер
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text=textmessages.startmessage)