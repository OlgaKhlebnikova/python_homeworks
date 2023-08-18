"""Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""
class Rectangle:
    """Класс прямоугольник.
Класс принимает длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат."""
    def __init__(self, _side_a, _side_b=0):
        """Инициализация класса"""
        self._side_a = _side_a
        if _side_b == 0:
            _side_b = _side_a
        self._side_b = _side_b

    def get_perimeter(self):
        """Метод возвращащает периметр квадрата или прямоугольника"""
        return 2 * (self._side_a + self._side_b)

    def get_area(self):
        """Метод возвращает площадь квадрата или прямоугольника"""
        return self._side_a * self._side_b

    def __add__(self, other):
        """Метод сложения"""
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """Метод вычитания"""
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):
        """Метод сравнения для равенства == """
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        """Метод сравнения для неравенства !="""
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        """Метод сравнения оператор больше >"""
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        """Метод сравнения оператора больше или равно >="""
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        """Метод сравнения оператора меньше < """
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """Метод сравнения для оператора меньше или равно <= """
        return self.get_area() <= other.get_area()

    def __str__(self):
        """Метод  возвращает строковое представление объекта"""

        return f'\nПлощадь прямоугольника со сторонами {self._side_a} и {self._side_b} = {self.get_area():.2f}'



rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)
print(rectangle1,rectangle2)

print(f'({rectangle1.get_area():.2f} = {rectangle2.get_area():.2f}):', rectangle1 == rectangle2)
print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):', rectangle1 != rectangle2)
print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):', rectangle1 > rectangle2)
print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):', rectangle1 <= rectangle2)
print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):', rectangle1 < rectangle2)
print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):', rectangle1 >= rectangle2)