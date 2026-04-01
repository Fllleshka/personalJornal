# Библиотека для асинхронного кода
import asyncio
# Из файла create_bot подгружаем bot
from createbot import bot, dp
# Обработка стартовых команд бота
from bot.startcommands import start_router

async def main():
    # Подключаем роутер, который отвечает за обработку первоначальных сообщений
    dp.include_router(start_router)
    # Начинаем постоянный опрос бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())