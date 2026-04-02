# Библиотека для работы с базой данных
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, ForeignKey, select, update, DATE, Time
# Импорт базового класса Base
from database.baseclass import Base
# Импорт библиотеки даты
from datetime import date, time

# Таблица "Сообщения"
class Messages(Base):
    __tablename__ = "messages"

    id_message: Mapped[int] = mapped_column(Integer, primary_key=True)
    day: Mapped[date] = mapped_column(DATE)
    time: Mapped[time] = mapped_column(Time)
    text: Mapped[str] = mapped_column(String, nullable=True)

def create_town(message: Messages, session) -> None:
    session.add(message)