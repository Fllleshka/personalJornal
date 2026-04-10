# Библиотека для работы с базой данных
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String, ForeignKey, select, update
# Импорт движка для работы с базой
from database.baseclass import engine
# Функция добавления данных в базу данных
def insert_user_dates_in_database(data):
    Session = sessionmaker(engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        try:
            create_users(Users(
                first_name=data['firstname'],
                middle_name=data['middlename'],
                last_name=data['lastname'],
                birth_date=data['age'],
                rating=0,
                id_telegram=data['telegramid'],
                id_town=find_id_in_table('towns', data['town']),
                id_kind=find_id_in_table('kinds', data['typesport']),
                id_level=find_id_in_table('levels', data['levelsport']),
                id_type=find_id_in_table('type', data['typeaccaunt']),
                id_place=find_id_in_table('places', data['place']),
                description=data['discription']), session)
        except:
            session.rollback()
            raise
        else:
            session.commit()
            logging.info("Данные успешно добавлены в базу данных")