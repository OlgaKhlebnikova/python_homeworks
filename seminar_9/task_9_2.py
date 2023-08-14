"""
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюу-угадайку
числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""


from random import randint


def func_enigma(func):
    def wrapper(q_num: int, attempts: int):
        q_num = q_num if 1 < q_num < 100 else randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else randint(1, 10)
        #print(q_num, attempts)
        res = func(q_num, attempts)
        return res
    return wrapper

@func_enigma
def attempts_count(q_num, attempts):
    while attempts > 0:
        num = int(input(f'Я загадал число от 1 до 100. Угадай:> '))
        if num == q_num:
            return "Угадал!"
        attempts -= 1
        # if num < q_num:
        #     print('Больше!')
        # else:
        #     print('Меньше!')
        print(f'осталось {attempts} попыток')
    return "Не угадал."


print(attempts_count(105, 25))