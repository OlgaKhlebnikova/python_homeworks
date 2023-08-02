"""Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [test, 9999].
Весь период (test января test года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

__all__ = ['check_date', 'leap_check']


def check_date(date: str):
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        elif 1 <= day <= 28 + leap_check(year):
            return True
        else:
            return False
    return False


def leap_check(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


if __name__ == '__main__':
    date = input("Введите дату: ")
    print(check_date(date))
