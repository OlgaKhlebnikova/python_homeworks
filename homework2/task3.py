from math import sqrt
"""
Задание №5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""
a, b, c = 3, 4, 5
d = b ** 2 - 4 * a * c


print('Задача 5. Решение уравнения даже если дискриминант отрицательный')
a = float(input('Введите a : '))
b = float(input('Введите b : '))
c = float(input('Введите c : '))

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f"Уравнение имеет два корня:  x1 = {round((-b + sqrt(d)) / (2 * a), 3)} ; x2 = {round((-b - sqrt(d)) / (2 * a), 3)} ")
elif d == 0:
    x1 = -b / (2 * a)
    print(f"Уравнение имеет один корень: x = {x1:.3f}")
else:
    real_part = -b / (2 * a)
    imaginary_part = sqrt(abs(d)) / (2 * a)
    x1 = complex(real_part, imaginary_part)
    x2 = complex(real_part, -imaginary_part)

    print(f'Уравнение имеет два комплексных корня: x1 = {x1:.3f}; x2 = {x2:.3f}')


