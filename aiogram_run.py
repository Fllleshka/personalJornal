# Библиотека для асинхронного кода
import asyncio
# Из файла create_bot подгружаем bot
from createbot import bot, dp
# Обработка стартовых команд бота
from bot.startcommands import start_router
# Импорт класса для работы с базой данных
from database.baseclass import baseclass
# Импорт базового класса Base
from database.baseclass import Base
# Импорт функции создания всех таблиц в БД
from database.tablesclass import create_all_databases
# Установка стартовых команд бота
from bot.startmenu import set_default_commands

async def main():
    # Подключаем роутер, который отвечает за обработку первоначальных сообщений
    dp.include_router(start_router)
    # Подгружаем первоначальные команды
    await set_default_commands(bot)

    # Вызываем базовый класс для работы с БД и выполняем метод
    dbclass = Base()
    if dbclass.checkdatabase() == True:
        print("База данных уже есть")
    else:
        # Заполняем базу данных таблицами
        create_all_databases()



    # Начинаем постоянный опрос бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())