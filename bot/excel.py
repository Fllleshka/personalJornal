# Библиотека для работы с файлом excel
from openpyxl import Workbook
from openpyxl.styles import Alignment
from openpyxl.styles import Border, Side, Font

# Импорт класса для работы с базой данных
from database.tablesclass import dbblass

class workwithexcel:

    def __init__(self, telegramid):
        self.telegramid = telegramid
        self.pathtofile = "database/excelfiles/" + str(self.telegramid) + ".xlsx"

    def createexcelfile(self, datestart, dateend):

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
        worksheet.column_dimensions['C'].width = 86

        # Объединяем ячейки и называем таблицу
        worksheet.merge_cells('A1:C1')

        cell = worksheet['A1']
        cell.value = "Таблица сообщений бота @PersonalJornalBot"
        cell.hyperlink = 'https://t.me/PersonalJournalBot'
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.font = Font(name='Arial', size=12, bold=True)



        # Озаглавливаем столбцы
        thin_border = Side(border_style="thin", color="000000")
        cell = worksheet['A3']
        cell.value = "№"
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = Border(top=thin_border, left=thin_border, right=thin_border, bottom=thin_border)
        cell = worksheet['B3']
        cell.value = "Дата сообщения"
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = Border(top=thin_border, left=thin_border, right=thin_border, bottom=thin_border)
        cell = worksheet['C3']
        cell.value = "Текст сообщения"
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = Border(top=thin_border, left=thin_border, right=thin_border, bottom=thin_border)

        startnumber = 4
        for elem in dates:

            # Номер строки
            cell = worksheet['A' + str(startnumber)]
            cell.value = elem[0]
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = Border(top=thin_border, left=thin_border, right=thin_border, bottom=thin_border)

            # Дата сообщения
            cell = worksheet['B' + str(startnumber)]
            cell.value = elem[1]
            cell.alignment = Alignment(horizontal='center', vertical='center')
            cell.border = Border(top=thin_border, left=thin_border, right=thin_border, bottom=thin_border)

            # Текст сообщения
            cell = worksheet['C' + str(startnumber)]
            cell.value = elem[2]
            cell.alignment = Alignment(wrap_text=True)
            cell.border = Border(top=thin_border, left=thin_border, right=thin_border, bottom=thin_border)

            startnumber += 1

        # Сохранение файла
        workbook.save(self.pathtofile)
        return self.pathtofile