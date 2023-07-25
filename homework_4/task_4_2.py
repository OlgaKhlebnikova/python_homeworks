"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление."""

def my_function(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, dict) or isinstance(value, list) or isinstance(value, set):
            result_dict[str(value)] = key
        else:
            result_dict[value] = key
    return result_dict


my_dict = my_function(один=True, два={"one", 1}, три=3, четыре={1, 1, 1, 2, 3})
print(f"{my_dict}\n")
for key, value in my_dict.items():
    print(f"{key} : {value}")
