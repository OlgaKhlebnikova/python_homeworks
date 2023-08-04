import os
from random import uniform, randint, choices
from string import ascii_lowercase
import random


def write_pair_nums(filename, lines):
    """Функцию заполняет файл
(добавляет в конец) случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.
"""

    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num} | {float_num:.2f}\n')






VOWELS = 'аеиоуыэюя'  # гласные русские буквы


def write_random_name(count_names: int):
    """
    Функцию, генерирует псевдоимена.
    Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
    Полученные имена сохраните в файл.
    """

    count = 0
    str_names = ""
    while count != count_names:
        word = choices(alfabet, k=randint(4, 7))
        if any(item in VOWELS for item in word):
            str_names += ''.join(word).capitalize() + '\n'
            count += 1
    with open('task7_2.txt', 'a', encoding='utf-8') as f:
        f.write(str_names)


# alfabet = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1)])
# write_random_name(6)




def my_func():
    """
    Функцию открывает на чтение созданные
    в прошлых задачах файлы с числами и именами.
    ✔ Перемножьте пары чисел. В новый файл сохраните
    имя и произведение:
    ✔ если результат умножения отрицательный, сохраните имя
    записанное строчными буквами и произведение по модулю
    ✔ если результат умножения положительный, сохраните имя
    прописными буквами и произведение округлённое до целого.
    ✔ В результирующем файле должно быть столько же строк,
    сколько в более длинном файле.
    ✔ При достижении конца более короткого файла,
    возвращайтесь в его начало.
    """

    with open('task7_1.txt', 'r', encoding='utf-8') as f_nums, \
            open('task7_2.txt', 'r', encoding='utf-8') as f_names:
        nums = f_nums.readlines()
        names = f_names.readlines()

    for_write = []
    long = max(len(nums), len(names))
    i = 0
    while len(nums) != len(names):
        if len(nums) > len(names):
            names.extend(names[:len(nums) - len(names)])
        else:
            nums.extend(nums[:len(names) - len(nums)])

    while i < long:
        name = names[i]
        num = nums[i]
        a, b = map(float, num.split('|'))
        mult = a * b

        if mult >= 0:
            for_write.append(f'{name.upper().rstrip()} - {round(mult)}\n')
        else:
            for_write.append(f'{name.lower().rstrip()} - {abs(mult)}\n')
        i += 1

    with open("task7_3.txt", 'w', encoding='utf-8') as f:
        f.writelines(for_write)




def func(ext, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096, files=42):
    """
    Функцию, которая создаёт файлы с указанным расширением.
    Функция принимает следующие параметры:
    ✔ расширение
    ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
    ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
    ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
    ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
    ✔ количество файлов, по умолчанию 42
    ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
    """

    for i in range(files):
        name = ''.join(choices(ascii_lowercase, k=randint(min_len, max_len))) + ext
        size = randint(min_rand_bytes, max_rand_bytes)
        with open(name, 'wb') as f:
            f.write(random.randbytes(size))



def func_2(files=10, **kwargs):
    """
    функцию генерирует файлы с разными расширениями.
    ✔ Расширения и количество файлов функция принимает в качестве параметров.
    ✔ Количество переданных расширений может быть любым.
    ✔ Количество файлов для каждого расширения различно.
    ✔ Внутри используйте вызов функции из прошлой задачи.
    """

    dct = kwargs
    val = []
    for k, v in dct.items():
        val.append(v)
    for i in range(files):
        ext = str(*choices(val))
        func(ext, files=1, min_len=6, max_len=30, min_rand_bytes=256, max_rand_bytes=4096)



def func_3(dir):
    """Функция генерируйте файлы в указанную директорию — отдельный параметр функции.
    ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
    (добавьте проверки).
    ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён."""
    my_path = os.getcwd() + dir
    try:
        os.makedirs(my_path)
        os.chdir(my_path)
    except FileExistsError:
        os.chdir(my_path)
    func_2(5, a='.txt', b='.json', c='.csv')
    os.chdir('..')




if __name__ == "__main__":
    write_pair_nums('task7_1.txt', 20)
    alfabet = ''.join([chr(char) for char in range(ord('а'), ord('я') + 1)])
    write_random_name(6)
    my_func()
    func('.txt')
    print(func_2(5, a='.txt', b='.doc', c='.exe'))
    func_3('_task6')
