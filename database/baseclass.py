# Импорт базового класса модели таблиц БД
from sqlalchemy.orm import DeclarativeBase
# Импорт данных для движка
from sqlalchemy import create_engine
# Библиотека для работы с файлами
import os

# Базовый класс наследуемый из класса библиотеки
class Base(DeclarativeBase):

    # Функция проверки наличия файла базы данных
    def checkdatabase(self):
        pathtodatabase = self.databaseurl()
        if(os.path.exists(pathtodatabase) == True):
            #print(f"База данных существует. Расположение: {pathtodatabase}")
            return True
        else:
            #print(f"База данных не существует. Расположение: {pathtodatabase}")
            return False

    # Функция вычисления правильного абсолютного пути до базы
    def databaseurl(self):
        # Получаем директорию скрипта
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Создаём полный путь к базе данных
        db_file_path = os.path.join(current_dir, 'database.db')
        return db_file_path

    # Создание пути для движка
    def pathforengine(self):
        pathtofile = self.databaseurl()
        pathtopaste = f"sqlite:///{pathtofile}"
        return pathtopaste

baseclass = Base()
# Создание движка для работы с БД
engine = create_engine(baseclass.pathforengine())