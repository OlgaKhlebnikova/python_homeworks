"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""
num_dec = int(input("Введите число: "))
print(f'Проверка {hex(num_dec)}')
symbol_hex = "0123456789abcdef"
res = ''
DIVIDER = 16
while num_dec > 0:
    res = symbol_hex[num_dec % DIVIDER] + res
    num_dec //= DIVIDER
print(f'Результат {res}')

num_dec_1 = int(input("Введите число: "))
while num_dec > 0:
    if num_dec_1 % DIVIDER < 10:
        res += str(num_dec % DIVIDER)
    elif num_dec_1 % DIVIDER == 10:
        res += "a"
    elif num_dec_1 % DIVIDER == 11:
        res += "b"
    elif num_dec_1 % DIVIDER == 12:
        res += "c"
    elif num_dec_1 % DIVIDER == 13:
        res += "d"
    elif num_dec_1 % DIVIDER == 14:
        res += "e"
    elif num_dec_1 % DIVIDER == 15:
        res += "f"
    num_dec_1 //= DIVIDER

print(f"Другой вариант решения: {res}")