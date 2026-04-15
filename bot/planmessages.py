# Библиотека для работы с Ботом
from aiogram import Router, types
# Импорт класса для работы с базой данных
from database.tablesclass import dbblass
# Импорт библиотеки для случайного выбора
import random

# Создаём роутер
messages_router = Router()

# Обработка входящего сообщения
@messages_router.message()
async def cmd_start(message: types.Message):
    dbblass.add_message_to_database(message)
    masssmile = ['👌', '👍', '🤝', '🫡', '🤌']
    textmessage = f"Записал " + random.choice(masssmile)
    await message.answer(text = textmessage)
