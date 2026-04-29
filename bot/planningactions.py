# Библиотека для работы со временем
from datetime import datetime, time
# Библиотека для работы с базой данных
from sqlalchemy.orm import sessionmaker
# Библиотека для выполнения функций по времени
#from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
# Библиотека для асинхронного кода
import asyncio

# Импорт движка для работы с базой
from database.baseclass import engine
# Импорт базового класса Base
from database.baseclass import Base
# Импорт класса User для получения данных из базы
from database.tablesclass import User
# Импорт бота для отправки сообщений
from createbot import bot

# ДЕКОРАТОР Время выполнения функции
def timetoactionfunc(func):
    def wrapper(*args):
        current_time = datetime.now()
        func(*args)
        print(f"{current_time.strftime("%H:%M:%S")}")
    return wrapper

class actions:

    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    # Функция получения данных и выполнения оповещения
    async def reminder(self, *args):
        #print(*args)
        # Получение всех клиентов из БД, кому требуется отправить уведомление
        clients = self.receivingdates(*args)
        #print(f"Clients: {len(clients)}")
        #print(f"\t\tClients: {clients}")
        # Отправка всем клиентам напоминания
        for elem in clients:
            #print(f"Element: {elem}")
            await self.sendmessage(elem.telegramid, args[1])

    # Запуск оповещений
    def run_morning_evening(self):
        # Утренние оповещения
        self.scheduler.add_job(self.reminder, "cron",
                               hour=5, minute=0, second=0, args = [self, "morning", 5])
        self.scheduler.add_job(self.reminder, "cron",
                               hour=6, minute=0, second=0, args = [self, "morning", 6])
        self.scheduler.add_job(self.reminder, "cron",
                               hour=7, minute=0, second=0, args = [self, "morning", 7])
        self.scheduler.add_job(self.reminder, "cron",
                               hour=8, minute=0, second=0, args = [self, "morning", 8])
        self.scheduler.add_job(self.reminder, "cron",
                               hour=9, minute=0, second=0, args = [self, "morning", 9])
        # Вечерние оповещения
        self.scheduler.add_job(self.reminder, "cron",
                               hour=20, minute=0, second=0, args=[self, "evening", 20])
        self.scheduler.add_job(self.reminder, "cron",
                               hour=21, minute=0, second=0, args=[self, "evening", 21])
        self.scheduler.add_job(self.reminder, "cron",
                               hour=22, minute=0, second=0, args=[self, "evening", 22])
        self.scheduler.add_job(self.reminder, "cron",
                               hour=23, minute=0, second=0, args=[self, "evening", 23])
        self.scheduler.add_job(self.reminder, "cron",
                               hour=0, minute=0, second=0, args=[self, "evening", 0])

        self.scheduler.start()

    # Получение данных из базы
    def receivingdates(self, *args):
        daytime = args[1]
        hour = args[2]
        #print(f"Значение {hour} переданное в функцию")
        # Время планирования на день
        timeonday = time(hour, 0, 0)
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            try:
                # получение всех объектов
                if daytime == "morning":
                    mass = session.query(User).where(User.timetoplanonday == timeonday).all()
                elif daytime == "evening":
                    mass = session.query(User).where(User.timetosummingup == timeonday).all()
                return mass
            except:
                return None

    # Функция отправки сообщения
    async def sendmessage(self, telegramid, daytime):
        print(f"\t\tКлиенту {telegramid} необходимо отправить напоминание.")
        if daytime == "morning":
            textformessage = "Доброе утро!\n\n Давай составим план на день!"
        else:

            textformessage = "Добрый вечер!\n\n Давай подведём итоги за день!"
        await bot.send_message(chat_id = telegramid, text = textformessage)


