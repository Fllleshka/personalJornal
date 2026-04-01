# Библиотека для работы с Ботом
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
# Библиотека для загрузки переменных окружения из .env
from decouple import config

# Инициируем объект бота, передавая ему parse_mode=ParseMode.HTML по умолчанию
bot = Bot(token = config('BOTKEY'),
          default = DefaultBotProperties(parse_mode=ParseMode.HTML))

# Инициируем объект бота
dp = Dispatcher()
