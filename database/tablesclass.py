# Библиотека для работы с базой данных
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, ForeignKey, Date, Time, func, update
# Импорт базового класса Base
from database.baseclass import Base
# Импорт библиотеки даты
from datetime import datetime, time, date
# Импорт движка для работы с базой
from database.baseclass import engine

# Таблица "Сообщения"
class Message(Base):
    __tablename__ = "messages"

    id_message: Mapped[int] = mapped_column(Integer, primary_key = True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    text: Mapped[str] = mapped_column(String, nullable=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.id_user"))

# Таблица "Пользователи"
class User(Base):
    __tablename__ = "users"

    id_user: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegramid: Mapped[int] = mapped_column(Integer)
    registrationdate: Mapped[datetime.date] = mapped_column(Date)
    timetoplanonday: Mapped[datetime.time] = mapped_column(Time)
    timetosummingup: Mapped[datetime.time] = mapped_column(Time)

def create_town(message: Message, session) -> None:
    session.add(message)
def create_user(user: User, session) -> None:
    session.add(user)

class databaseclass:

    # Главная функция генерации таблиц и данных в БД
    def create_all_databases(self):
        # Создаём сессию
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            # Создаём таблицу сообщения в базе
            create_town(Message(), session)
            # Создаём таблицу сообщения в базе
            create_user(User(), session)

        print("База данных сгенерирована")

    # Проверка пользователя на присутствие в базе данных
    def check_user_in_database(self, telegramiduser):
        # Создаём сессию
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            user = session.query(User).filter_by(telegramid = telegramiduser).first()
        if user == None:
            return False
        else:
            return user.id_user

    # Получение данных из таблицы Users
    def selecttimesfromusers(self, telegramid):
        # Создаём сессию
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            results = session.query(User).filter(
                User.telegramid == telegramid
            ).first()
        return [results.timetoplanonday.strftime("%H:%S"), results.timetosummingup.strftime("%H:%S")]


    # Вставка данных о новом пользователе при команде /start
    def create_new_user(self, message):
        # Время планирования на день
        timetoplanonday = time(8, 0, 0)
        # Время подведения итогов дня
        timetosummingup = time(22, 0, 0)

        # Создаём сессию
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            newuser = User(
                telegramid = message.chat.id,
                registrationdate = date.today(),
                timetoplanonday = timetoplanonday,
                timetosummingup = timetosummingup
            )
            session.add(newuser)
            session.commit()
        print(f"Создание пользователя {message.chat.id} успешно")

    # Вставка сообщения от пользователя в базу данных
    def add_message_to_database(self, message):

        # Создаём сессию
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            newmessage = Message(
                text = message.text,
                id_user = self.check_user_in_database(message.chat.id)
            )
            session.add(newmessage)
            session.commit()

    # Обновление времени напоминания
    def updatetime(self, telegramiduser, daypart, newtime):
        # Формируем запрос
        if daypart == 'morning':
            request = update(User).where(
                User.id_user == self.check_user_in_database(
                    telegramiduser)).values(timetoplanonday=time(newtime, 0, 0))
        else:
            request = update(User).where(
                User.id_user == self.check_user_in_database(
                    telegramiduser)).values(timetosummingup=time(newtime, 0, 0))

        # Выполнение запроса
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            session.execute(request)
            session.commit()

    # Получение всех записей по данному аккаунту
    def selectalldates(self, datestart, dateend, telegramid):

        # Создаём сессию
        Session = sessionmaker(engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            results = session.query(Message).filter(
            Message.created_at >= datestart, Message.created_at <= dateend
            ).all()
        if results == None:
            return None
        else:
            resultdates = []
            for elem in results:
                resultdates.append([results.index(elem) + 1, elem.created_at, elem.text])
            return resultdates


dbblass = databaseclass()