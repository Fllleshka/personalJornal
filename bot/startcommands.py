# Библиотека для работы с Ботом
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
# Баблиотека работы с датой
import datetime

# Импорт класса для текстовых сообщений
from dates.startcommands import textmessages
# Импорт класса кнопок
from dates.buttons import buttonstext
# Импорт функции для вычисления названия аккаунта человека
from bot.users.commandusers import create_appeal
# Импорт класса для работы с базой данных
from database.tablesclass import dbblass
# Импорт класса для кнопок
from bot.markups import markup as markupclass
# Импорт класса для работы с файлом excel
from bot.excel import workwithexcel

# Создаём роутер
start_router = Router()

# Обработка команды /start
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    # Получаем имя
    name = create_appeal(message)
    # Проверка на существование аккаунта
    if dbblass.check_user_in_database(message.chat.id) == False:
        textmessage = f"Привет, {name}!\n" + textmessages.startmessage + textmessages.startmessage2
        dbblass.create_new_user(message)
        await message.answer(text = textmessage)
    else:
        datesfromdabase = dbblass.selecttimesfromusers(message.chat.id)
        textmessage = f"Снова здравствуй, {name}!\n"
        textmessage += textmessages.startmessage3
        textmessage += datesfromdabase[0] + "\n\n"
        textmessage += textmessages.startmessage4
        textmessage += datesfromdabase[1] + "\n\n"
        await message.answer(text = textmessage)


# Обработка команды /settings
@start_router.message(Command('settings'))
async def cmd_settings(message: Message):
    textmessage = textmessages.settingsmessage
    inline_button = [
        [types.InlineKeyboardButton(text = buttonstext.morningtime, callback_data = "button_morning")],
        [types.InlineKeyboardButton(text = buttonstext.eveningtime, callback_data = "button_evening")]
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard = inline_button)
    await message.answer(text=textmessage, reply_markup=markup)

# Обработка callbackов кнопок
@start_router.callback_query(F.data.startswith("button_"))
async def callback_buttons(callback: types.CallbackQuery):
    button = callback.data.split("_")[1]

    match(button):
        case "morning":
            # Редактируем текст и вставляем новые кнопки
            await callback.message.edit_text(
                f"Вы выбрали: ✅ Утро! ✅",
                reply_markup = markupclass.returninlinemarkup(button)
            )
        case "evening":
            # Редактируем текст и вставляем новые кнопки
            await callback.message.edit_text(
                f"Вы выбрали: ✅ Вечер! ✅",
                reply_markup = markupclass.returninlinemarkup(button)
            )
        case _:
            pass

# Обработка callbackов по оповещению
@start_router.callback_query(F.data.startswith("new_time_"))
async def callback_fruits(callback: types.CallbackQuery):
    # Выделяем данные
    newtime = callback.data.split("_")
    splittime = newtime[-1].split(":")
    telegramiduser = callback.message.chat.id

    # Редактируем сообщение
    await callback.message.edit_text(
        f"Вы выбрали: ⏳{newtime[-1]}⌛️",
        reply_markup=None
    )

    # Функция обновления времени в базе
    if newtime[2] == 'morning':
        dbblass.updatetime(telegramiduser, 'morning', int(splittime[0]))
    elif newtime[2] == 'evening':
        dbblass.updatetime(telegramiduser, 'evening', int(splittime[0]))
    else:
        pass

    await callback.message.answer(text = "Обновил", reply_markup=None)

# Обработка команды /exportdates
@start_router.message(Command('exportdates'))
async def cmd_exportdates(message: Message):

    textmessage = "Выберите промежуток за которы нужно выгрузить данные."
    inline_button = [
        [types.InlineKeyboardButton(text=buttonstext.lastmonth, callback_data="exportexcel_1")],
        [types.InlineKeyboardButton(text=buttonstext.lastthreemoth, callback_data="exportexcel_3")],
        [types.InlineKeyboardButton(text=buttonstext.lastsixmonth, callback_data="exportexcel_6")],
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=inline_button)
    await message.answer(text=textmessage, reply_markup=markup)

# Обработка callbackов кнопок /exportdates
@start_router.callback_query(F.data.startswith("exportexcel_"))
async def callback_buttons_excel(callback: types.CallbackQuery):

    data = callback.data
    month = data.split("_")

    #print(f"Нажата кнопка: {month[1]}")

    today = datetime.datetime.today()
    match(month[1]):
        case '3':
            newdate = today - datetime.timedelta(days = 90)
        case '6':
            newdate = today - datetime.timedelta(days = 180)
        case _:
            newdate = today

    datestart = datetime.date(newdate.year, newdate.month, 1)
    #print(f"Дата начала: {datestart}")
    dateend = datetime.date(today.year, today.month, today.day)
    #print(f"Дата окончания: {dateend}")

    telegramiduser = callback.message.chat.id
    file = workwithexcel(telegramiduser)
    filetosend = FSInputFile(file.createexcelfile(datestart, dateend))

    textmessage = "Вот ваш файл"
    await callback.message.answer_document(filetosend, caption = textmessage)