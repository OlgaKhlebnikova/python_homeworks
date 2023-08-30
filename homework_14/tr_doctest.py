import doctest
class Triangle:
    """Класс может рассчитывать площадь по сторонам треугольника
    и сравнивать треугольники по площадям
    >>> triangle_1 = Triangle(5, 4, 6)
    >>> print(triangle_1)
    Треугольник со сторонами: (5, 4, 6)
    >>> print(triangle_1.square())
    9.92
    >>> triangle_2 = Triangle(5, 4, -2)
    Traceback (most recent call last):
    ...
    AttributeError: Стороны треугольника должны быть положительными
    >>> triangle_3 = Triangle(6, 5, 4)
    >>> print(triangle_1 == triangle_3)
    True
    >>> triangle_4 = Triangle(5, 4, 7)
    >>> print(triangle_1 == triangle_4)
    False
    """

    def __init__(self, a, b, c):
        if a < 0 or b < 0 or c < 0:
            raise AttributeError('Стороны треугольника должны быть положительными')
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f'Треугольник со сторонами: {(self.a, self.b, self.c)}'

    def square(self):
        per = (self.a + self.b + self.c) / 2
        square_ = (per * (per - self.a) * (per - self.b) * (per - self.c)) ** 0.5
        return round(square_, 2)

    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __hash__(self):
        return hash((self.a, self.b, self.c))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
