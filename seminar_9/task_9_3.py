"""
Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""

import json


def decor(func):
    write_dct = {}

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        filename = f'{func.__name__}.json'
        write_dct["arguments"] = f'{args[0]} , {args[1]}'
        for key, value in kwargs.items():
            write_dct[key] = value
        write_dct["result"] = result
        with open(filename, 'a', encoding="utf-8") as js_f:
            json.dump(write_dct, js_f, indent=2)
        return result

    return wrapper


@decor
def power_х(x, y):
    return x ** y


print(power_х(2, 10))
print(power_х(5, 3))