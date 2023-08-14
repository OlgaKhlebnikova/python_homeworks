"""
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""

def func_enigma(q_num, attempts):

    def attempts_count():
        nonlocal attempts
        while attempts > 0:
            num = int(input(f'Я загадал число от 1 до 100. Угадай:> '))
            if num == q_num:
                return "Угадал!"
            attempts -= 1
            print(f'осталось {attempts} попыток')
        return "Не угадал."
    return attempts_count


res = func_enigma(15, 5)

print(res())



