"""
Задание №5
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр
прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""
class Rectangle:
    """Класс прямоугольник.
Класс принимает длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат."""

    def __init__(self, side_a, side_b=0):
        """Инициализация класса"""
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        """Метод возвращащает периметр квадрата или прямоугольника"""
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        """Метод возвращает площадь квадрата или прямоугольника"""
        return self.side_a * self.side_b

    def __add__(self, other):
        """Метод сложения"""
        # (self.side_a + other.side_a, self.side_b + other.side_b)
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        """Метод вычитания"""
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)
    def __str__(self):
        """Метод  возвращает строковое представление объекта"""
        res = f'Периметр прямоугольника со сторонами {self.side_a} и {self.side_b} = {self.get_perimeter():.2f} '
        return res

rectangle1 = Rectangle(7.3)
rectangle2 = Rectangle(5.6, 10.2)
rectangle3 = rectangle1 + rectangle2
rectangle4 = rectangle3 - rectangle2


print(rectangle1)
print(rectangle2)
print(rectangle3)
print(rectangle4)