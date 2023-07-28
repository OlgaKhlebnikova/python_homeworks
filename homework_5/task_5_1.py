# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def file_path(data):
    """Функция, которая принимает на вход строку — абсолютный путь до файла.
    Возвращает кортеж из трёх элементов: путь, имя файла, расширение файла"""
    data = data.replace(".", " ").replace("\\", " ")
    *way, name, extension = data.split()
    res = "\\".join(way), name, extension
    return res


path = "D:\ОБУЧЕНИЕ GB\Python погружение\python_homeworks\homework_5\task_5_1.py"
print(file_path(path))
