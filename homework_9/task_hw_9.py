"""Напишите следующие функции:
1Нахождение корней квадратного уравнения
2Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
3Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
4Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
"""
from math import sqrt
from random import randint
import csv
from typing import Callable
import json
from pathlib import Path
import datetime

def give_file_numbers():
    f_line = randint(100, 1000)
    with open('random_numbers_file.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for _ in range(f_line):
            writer.writerow([randint(1, 99), randint(1, 99), randint(1, 99)])


def decor_equation(func: Callable):
    give_file_numbers()

    def wrapper(*args, **kwargs):
        with open('random_numbers_file.csv', 'r', encoding='UTF-8') as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for el in reader:
                if el and el[0] != 0:
                    func(*el)
                    #print(func(*el))

    return wrapper


def save_to_json(func):
    j_file = Path(f"{func.__name__}.json")
    my_res = {}
    if j_file.is_file():
        with open(j_file, 'r', encoding='UTF-8') as file:
            my_res = json.load(file)
    else:
        with open(j_file, 'w', encoding='UTF-8') as file:
            json.dump(my_res, file)

    def wrapper(*args):
        roots = func(*args)
        solve_dict = {'a': args[0], 'b': args[1], 'c': args[2], 'roots': roots}
        res_key = f'{datetime.datetime.now().strftime("%d-%m-%Y-%H.%M.%S")}'
        my_res[res_key] = my_res.get(res_key) + [solve_dict] if my_res.get(res_key) else [solve_dict]
        with open(j_file, 'w', encoding='UTF-8', ) as file:
            json.dump(my_res, file, indent=2, ensure_ascii=False)
        return roots

    print(f"Решение квадратных уравнений  добавлено в файл {j_file}")
    return wrapper


@decor_equation
@save_to_json
def give_roots(a, b, c):
    d = b ** 2 - 4 * a * c

    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return f"x1 ={x1:.3f} x2 ={x2:.3f}"
    elif d == 0:
        x1 = -b / (2 * a)
        return f"x1 = {x1:.3f}"
    else:
        return 'Корней нет'


print(give_roots())
