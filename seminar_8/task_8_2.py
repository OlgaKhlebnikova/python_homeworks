# """
# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
#
# """
# import json
#
#
# def fun_dump_json():
#
#     name = input("введите имя:> ")
#     user_id = input("введите id:> ")
#     level = int(input('введите уровень доступа (1-7):> '))
#
#     my_dct = {
#         "level": level,
#         "id": user_id,
#         "name": name,
#         }
#
#     with open('task8_2.json', "a", encoding='utf-8') as js_f:
#         json.dump(my_dct, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)
#
#
#
#
#
# s = 'n'
# while s != 'y':
#     fun_dump_json()
#     s = input('выход y/n :>')

"""
Задание №2
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""

import json


def fun_dump_json():
    # name = input("введите имя:> ")
    # user_id = input("введите id:> ")
    # level = int(input('введите уровень доступа (1-7):> '))
    name = "Петя"
    user_id = "002"
    level = 4

    with open('task8_2.json', "r", encoding='utf-8') as f:
        res = json.load(f)

    my_dct = {
        "level": level,
        "id": user_id,
        "name": name,
    }

    with open('task8_2.json', "w", encoding='utf-8') as js_f:
        res.append(my_dct)
        json.dump(res, js_f, indent=2, separators=(',', ':'), ensure_ascii=False)


lst = []
with open('task8_2.json', "w", encoding='utf-8') as js_f:
    json.dump(lst, js_f)

s = 'n'
while s != 'y':
    fun_dump_json()
    s = input('выход y/n :>')