"""
Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""
def func(param):
    def deco(f):
        def wrapper(*args, **kwargs):
            count = 0
            for _ in range(param):
                res = f(args[0], args[1])
                count += 1
            return res, count

        return wrapper

    return deco


@func(10)
def summ(x, y):
    return x + y


print(summ(2, 2))
