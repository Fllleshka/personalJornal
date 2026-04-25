# Библиотека для работы со временем
from datetime import datetime, time
# Библиотека для работы с базой данных
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
# Библиотека для выполнения функций по времени
from apscheduler.schedulers.background import BackgroundScheduler

# Импорт движка для работы с базой
from database.baseclass import engine
# Импорт базового класса Base
from database.baseclass import Base

from database.tablesclass import User

# ДЕКОРАТОР Время выполнения функции
def timetoactionfunc(func):
    def wrapper(*args):
        current_time = datetime.now()
        func(*args)
        print(f"{current_time.strftime("%H:%M:%S")}")
    return wrapper

class actions:

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def morning_reminder(self, *args):
        print(f"{datetime.now()}\t\t{args[1]}"
              f"Job Done!")

        # Получение всех клиентов из БД, кому требуется отправить уведомление
        clients = self.receivingdates(args[1])
        for elem in clients:
            print(elem.id_user)
        # Отправка всем клиентам напоминания

    # Запуск оповещений утренних
    def runmorning(self):
        self.scheduler.add_job(self.morning_reminder, "cron",
                               hour=5, minute=0, second=0, args = [self, 5])
        self.scheduler.add_job(self.morning_reminder, "cron",
                               hour=6, minute=0, second=0, args = [self, 6])
        self.scheduler.add_job(self.morning_reminder, "cron",
                               hour=7, minute=0, second=0, args = [self, 7])
        self.scheduler.add_job(self.morning_reminder, "cron",
                               hour=8, minute=0, second=0, args = [self, 8])
        self.scheduler.add_job(self.morning_reminder, "cron",
                               hour=9, minute=0, second=0, args = [self, 9])
        self.scheduler.start()

    # Получение данных из базы
    def receivingdates(self, hour):
        print(f"Значение {hour} переданное в функцию")
        # Время планирования на день
        timetoplanonday = time(hour, 0, 0)
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session(autoflush=False, bind=engine) as session:
            try:
                # получение всех объектов
                mass = session.query(User).where(User.timetoplanonday == timetoplanonday)
                mass = session.query(User).where(User.timetoplanonday == timetoplanonday)
                return mass
            except:
                return None

    # Функция отправки сообщения
    def sendmessage(self, telegramid):
        pass