"""
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
from math import pi


class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_len(self):
        return 2 * pi * self._radius

    def get_area(self):
        return pi * self._radius ** 2


circle = Circle(7)
print(f'Длина окружности = {circle.get_len():.3f}, \nПлощадь окружности = {circle.get_area():.3f}')