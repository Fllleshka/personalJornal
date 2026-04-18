# Библиотека для работы с Ботом
from aiogram import types

# Класс для кнопок
class inlinemarkup:

    def returninlinemarkup(self, daytime):

        match (daytime):
            case "morning":
                buttonlist = [
                    [types.InlineKeyboardButton(text='05:00',
                                                callback_data='new_time_morning_' + '05:00')],
                    [types.InlineKeyboardButton(text='06:00',
                                                callback_data='new_time_morning_' + '06:00')],
                    [types.InlineKeyboardButton(text='07:00',
                                                callback_data='new_time_morning_' + '07:00')],
                    [types.InlineKeyboardButton(text='08:00',
                                                callback_data='new_time_morning_' + '08:00')],
                    [types.InlineKeyboardButton(text='09:00',
                                                callback_data='new_time_morning_' + '09:00')]
                ]
            case "evening":
                buttonlist = [
                    [types.InlineKeyboardButton(text='20:00',
                                                callback_data='new_time_evening_' + '20:00')],
                    [types.InlineKeyboardButton(text='21:00',
                                                callback_data='new_time_evening_' + '21:00')],
                    [types.InlineKeyboardButton(text='22:00',
                                                callback_data='new_time_evening_' + '22:00')],
                    [types.InlineKeyboardButton(text='23:00',
                                                callback_data='new_time_evening_' + '23:00')],
                    [types.InlineKeyboardButton(text='00:00',
                                                callback_data='new_time_evening_' + '00:00')]
                ]
            case _:
                buttonlist = []

        return types.InlineKeyboardMarkup(inline_keyboard = buttonlist)

markup = inlinemarkup()