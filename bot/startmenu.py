# Библиотека для работы с Ботом
from aiogram.types import BotCommand, BotCommandScopeDefault

# Функция добавления меню в боте
async def set_default_commands(bot):
    commands = [
        BotCommand(command = "start", description = 'Начать сначала'),
        BotCommand(command = "settings", description = 'Настройка расписания')
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
    print("Команды успешно добавлены")