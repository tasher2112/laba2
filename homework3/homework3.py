from datetime import datetime
def birthday():
    while True:
        birthday_date_str = input("Введите дату рождения в формате дд/мм/гггг(например 01/12/1985): ")
        try:
            birthday_date = datetime.strptime(birthday_date_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Неверный ввод! Повторите ещё раз!")
    today = datetime.now()
    age = today.year - birthday_date.year
    if (today.month, today.day) < (birthday_date.month, birthday_date.day):
        age -= 1
    print("Ваш возраст:", age, " лет")
birthday()