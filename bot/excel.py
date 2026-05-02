# Библиотека для работы с файлом excel
from openpyxl import Workbook
from openpyxl.styles import Alignment
# Баблиотека работы с датой
import datetime

# Импорт класса для работы с базой данных
from database.tablesclass import dbblass


class workwithexcel:

    def __init__(self, telegramid):
        self.telegramid = telegramid
        self.pathtofile = "database/excelfiles/" + str(self.telegramid) + ".xlsx"

    def createexcelfile(self):
        today = datetime.datetime.today()
        datestart = datetime.date(today.year, today.month, 1)
        #print(f"Дата начала: {datestart}")
        dateend = datetime.date(today.year, today.month, today.day)
        #print(f"Дата окончания: {dateend}")

        # Получение данных из базы
        dates = dbblass.selectalldates(datestart, dateend, self.telegramid)
        #print(f"Данные: {dates}")


        # Формирование файла excel
        workbook = Workbook()
        worksheet = workbook.active

        # Установка названия листа
        worksheet.title = str(datestart) + " | " + str(dateend)

        # Выставляем ширину столбцов
        worksheet.column_dimensions['A'].width = 3
        worksheet.column_dimensions['B'].width = 18
        worksheet.column_dimensions['C'].width = 65
        # Озаглавливаем столбцы
        worksheet['A3'] = "№"
        worksheet['B3'] = "Дата сообщения"
        worksheet['C3'] = "Текст сообщения"

        startnumber = 4
        for elem in dates:

            # Номер строки
            cell = worksheet['A' + str(startnumber)]
            cell.value = elem[0]

            # Дата сообщения
            cell = worksheet['B' + str(startnumber)]
            cell.value = elem[1]

            # Текст сообщения
            cell = worksheet['C' + str(startnumber)]
            cell.value = elem[2]
            cell.alignment = Alignment(wrap_text=True)

            startnumber += 1
            '''for column in ['A', 'B', 'C']:
                numbercell = column + str(elem[0] + 3)
                print(f"NumberCell: {numbercell}")
                cell = worksheet[str(numbercell)]
                print(f"\tCell: {cell}")
                print(f"\tCell: {cell}")
                cell.value = 123
                cell.alignment = Alignment(wrap_text=True)


            worksheet.append([elem[0], elem[1], elem[2]])'''

            # Текст с переносом
            #text = "Первая строка\nВторая строка"
            #cell = ws['A1']
            #cell.value = text

            # ВАЖНО: Включаем перенос текста в стиле ячейки
            #cell.alignment = Alignment(wrap_text=True)

        # Сохранение файла
        workbook.save(self.pathtofile)
        return self.pathtofile