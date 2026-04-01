# Библиотека для работы с Ботом
from types import NoneType
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove
# Библиотека для загрузки переменных окружения из .env
from decouple import config
# Создаём роутер
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Привет!")