# Вычисления обращения к пользователю
def create_appeal(message):
    try:
        name = message.from_user.first_name + " " + message.from_user.last_name
    except:
        name = "Друг"
    return name