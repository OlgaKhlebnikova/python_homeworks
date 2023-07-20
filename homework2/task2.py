import fractions, re

import math

"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

str_1: str = input("Введите 2 числа для составления 1-ой дроби(пр: a/b) ")
str_2: str = input("Введите 2 числа для составления 2-ой дроби(пр: a/b) ")
fraction_1 = re.split('/', str_1)
fraction_2 = re.split('/', str_2)

significant_1 = int(fraction_1[0])
denominator_1 = int(fraction_2[1])
significant_2 = int(fraction_2[0])
denominator_2 = int(fraction_2[1])

if denominator_1 == denominator_2:
    nod_1 = math.gcd((significant_1 + significant_2), (denominator_1 +denominator_2))
    if (significant_1 + significant_2) % denominator_1 == 0:
        print(f'Сумма дробей = {int((significant_1 + significant_2) / denominator_1)}')
    else:
        print(f'Сумма дробей = {int(significant_1 + significant_2)}/{denominator_1}')
else:
    cd = int(denominator_1 * denominator_2 / denominator_1, denominator_2)
    rn = int(cd / denominator_1 * significant_1 + cd / denominator_2 * significant_2)
    if int(rn / math.gcd(rn, cd)) == int(cd / math.gcd(rn, cd)):
        print(f'Сумма дробей = {int(rn / math.gcd(rn, cd) / cd / math.gcd(rn, cd))}')

    else:
        print(f'Сумма дробей = {int(rn / math.gcd(rn, cd))}/{int(cd / math.gcd(rn, cd))}')

    # произведение дробей


e = significant_1 * significant_2

f = denominator_1 * denominator_2
print(f'Произведение дробей = {int(e / math.gcd(e, f))}/{int(f / math.gcd(e, f))}')
fraction_etalon_1 = fractions.Fraction(significant_1, denominator_1)
fraction_etalon_2 = fractions.Fraction(significant_2, denominator_2)
print(f"Проверка: \n\tСумма дробей = {fraction_etalon_1 + fraction_etalon_2} "
      f"\n\tПроизведение дробей = {fraction_etalon_1 * fraction_etalon_2}")
