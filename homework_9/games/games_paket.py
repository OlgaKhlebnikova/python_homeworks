from random import randint
from sys import argv


def guess_number(start, stop, count):
    """
    Функция принимает на вход три целых числа:
    нижнюю и верхнюю границу и количество попыток.
    Внутри генерируется случайное число в указанных
    границах и пользователь должен угадать его за заданное число попыток.
    Функция выводит подсказки “больше” и “меньше”.
    Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
    """
    num = randint(start, stop + 1)
    i = 0
    while count > i:
        u_num = int(input(f"введите число в диапазоне от {start} до {stop}:>"))
        if u_num > num:
            print('меньше!')
        elif u_num < num:
            print('больше!')
        else:
            print('Угадал!')
            return True
        i += 1
    return False

def guess_number_new(argums):
    """возможность запуска функции “угадайки”
из модуля в командной строке терминала."""
    num = randint(argums[0], argums[1])
    i = 0
    while argums[2] > i:
        u_num = int(input(f"введите число в диапазоне от {argums[0]} до {argums[1]}:>"))
        if u_num > num:
            print('меньше!')
        elif u_num < num:
            print('больше!')
        else:
            print('Угадал!')
        return True
        i += 1
    return False

def riddle(qws, ans, count):
    """Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны."""
    print(f"загадка: {qws}")
    print(f"варианты ответов: {ans}")
    i = 0
    while count >= i:
        u_ans = input(f"введите ваш ответ:>")
        if u_ans == ans[0]:
            print(f'Правильно! Угадал за {i + 1} попытку')
            return i + 1
        else:
            print('Не угадал!')
            i += 1
            if i == count:
                return 0


def riddle_2(dct):
    '''Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение'''

    for k, v in dct.items():
        print(riddle(k, v, 3))

dct = {"В чем сила: ": ['в правде', 'в деньгах', 'в силе'],
       "Не лает, не кусает, в дом не пускает": ['замок', 'охранник', 'собака']}
_dct = {}
def riddle_3(que, count):
    print(que)
    a = "в правде"

    i = 0
    while count > i:
        ans = input("Напишите ответ>")
        if ans == a:
            _dct[i + 1] = "Вы угадали"
            return
        else:
            _dct[i + 1] = "Не угадали"
            i += 1


def battle_queens(position: list) -> bool:
    """Определяет, есть ли среди ферзей пара бьющих друг друга."""
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True

    else:
        return False

def func_enigma(q_num, attempts):
    """
    Задание №1
    Создайте функцию-замыкание, которая запрашивает два целых
    числа:
    ○ от 1 до 100 для загадывания,
    ○ от 1 до 10 для количества попыток
    Функция возвращает функцию, которая через консоль просит
    угадать загаданное число за указанное число попыток.
    """
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


if __name__ == '__main__':
    print(guess_number(1, 3, 3))
    argums = [int(el) for el in argv[1:]]
    print(guess_number_new(argums))
    print(riddle("Не лает, не кусает, в дом не пускает",
                 ['замок', 'охранник', 'собака'], 3))
    riddle(dct)
    riddle_3("В чем сила:", 3)
    print(_dct)
    position_1 = (1, 3), (2, 6), (4, 1), (7, 7), (5, 8), (8, 2), (3, 4), (6, 5)
    print(battle_queens(position_1))
    position_2 = (1, 4), (2, 6), (4, 1), (7, 7), (5, 8), (8, 2), (3, 4), (6, 5)
    print(battle_queens(position_2))
    res = func_enigma(15, 5)
    print(res())
    print(attempts_count(105, 25))