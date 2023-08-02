"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""


from datetime import datetime
from sys import argv
from task_6_1_sem import *
def date_validate(date: str):
    """Функция проверки даты"""
    try:
        print(date)
        datetime.strptime(date, "%d.%m.%Y").date()
        return True
    except:
        print("Некорректная дата")
        return False



if __name__ == '__main__':
    print("Запускать в терминале (передать дату в формате ДД.ММ.ГГ)")
    print(date_validate(*(argv[1:])))