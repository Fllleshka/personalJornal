# Библиотека для работы с базой данных
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, ForeignKey, select, update, DATE, Time
# Импорт базового класса Base
from database.baseclass import Base
# Импорт библиотеки даты
from datetime import date, time
# Импорт движка для работы с базой
from database.baseclass import engine

# Таблица "Сообщения"
class Messages(Base):
    __tablename__ = "messages"

    id_message: Mapped[int] = mapped_column(Integer, primary_key=True)
    day: Mapped[date] = mapped_column(DATE)
    time: Mapped[time] = mapped_column(Time)
    text: Mapped[str] = mapped_column(String, nullable=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"))
# Таблица "Пользователи"
class Users(Base):
    __tablename__ = "users"

    id_user: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegramid: Mapped[int] = mapped_column(Integer)
    registrationdate: Mapped[date] = mapped_column(DATE)
    timetoplanonday: Mapped[time] = mapped_column(Time)
    timetosummingup: Mapped[time] = mapped_column(Time)

def create_town(message: Messages, session) -> None:
    session.add(message)
def create_user(user: Users, session) -> None:
    session.add(user)

# Главная функция генерации таблиц и данных в БД
def create_all_databases():
    # Создаём сессию
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        # Создаём таблицу сообщения в базе
        create_town(Messages(), session)
        # Создаём таблицу сообщения в базе
        create_user(Users(), session)

    print("База данных сгенерирована")