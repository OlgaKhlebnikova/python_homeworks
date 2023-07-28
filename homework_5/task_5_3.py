""""Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def fibonacci(n):
    """Функция вычисления числа Фибоначчи"""
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_generator(n):
    """Функция генератор чисел Фибоначчи"""
    for i in range(1, n + 1):
        yield f"{i}-e число ряда Фибоначчи = {fibonacci(i)}"


num = 7
for el in fib_generator(num):
    print(el)
