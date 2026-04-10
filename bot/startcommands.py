# Библиотека для работы с Ботом
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove
# Импорт класса для текстовых сообщений
from dates.startcommands import textmessages
# Импорт класса кнопок
from dates.buttons import buttonstext
# Импорт функции для вычисления названия аккаунта человека
from bot.users.commandusers import create_appeal
# Импорт класса для работы с базой данных
from database.tablesclass import dbblass


# Создаём роутер
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    name = create_appeal(message)
    textmessage = f"Привет, {name}!\n" + textmessages.startmessage + textmessages.startmessage2
    dbblass.create_new_user(message)
    await message.answer(text = textmessage)

@start_router.message(Command('settings'))
async def cmd_settings(message: Message):
    textmessage = textmessages.settingsmessage
    inline_button = [
        [types.InlineKeyboardButton(text = buttonstext.morningtime, callback_data = "123")],
        [types.InlineKeyboardButton(text = buttonstext.eveningtime, callback_data = "123")]
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard = inline_button)
    await message.answer(text=textmessage, reply_markup=markup)