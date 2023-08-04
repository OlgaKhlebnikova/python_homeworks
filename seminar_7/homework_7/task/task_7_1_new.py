# Решить задачи, которые не успели решить на семинаре.
# Напишите функцию группового переименования файлов. Она должна:
# Принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# Принимать параметр количество цифр в порядковом номере.
# Принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# Принимать параметр расширение конечного файла.
# Принимать диапазон сохраняемого оригинального имени.
# - Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# - К ним прибавляется желаемое конечное имя, если оно передано.
# - Далее счётчик файлов и расширение.
# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import os


def create_counter(num):
    limit = 99999
    countdown = 1 if num == 1 else 10 ** (num - 1)
    for i in range(countdown, limit):
        yield i


def rename_files(serial_number, first_extension, second_extension, original_range=(1, 0), end_filename=""):
    """
    :param serial_number: Кол-во цифр, при переименовании в конце имени добавляется порядковый номер.
    :param first_extension: Принимает параметр расширение исходного файла.(без точки)
    :param second_extension: Принимает параметр расширение конечного файла.(без точки)
    :param original_range: Принимает диапазон сохраняемого оригинального имени.(по умолчанию не берет старое имя )
    :param end_filename: Принимает параметр желаемое конечное имя файлов.(по умолчанию не добавляет)
    """
    serial_number = create_counter(serial_number)
    dir_list = os.listdir()
    take_from, take_up = original_range

    for file_name in dir_list:
        if ("." + first_extension) in file_name:
            new_name = file_name.split(".")[0][take_from - 1:take_up] + end_filename + "_" + str(
                next(serial_number)) + "." + second_extension
            os.rename(file_name, new_name)


rename_files(1, "txt", "txt", [1, 3], end_filename="_new")
