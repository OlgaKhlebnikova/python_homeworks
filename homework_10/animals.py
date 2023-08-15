"""
Задание №6
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, kind, name, age):
        self._kind = kind
        self._name = name
        self._age = age

    def get_kind(self):
        return f'Вид : {self._kind}'

    def get_name(self):
        return f'Имя животного: {self._name}'

    def get_age(self):
        return f'Возраст животного: {self._age}'

    def up_age(self):
        self._age += 1
        return f'Возраст животного: {self._age} лет'


class Fishes(Animal):

    def __init__(self, kind, name, age, size):
        super().__init__(kind, name, age)
        self._size = size

    def get_specific(self):
        return f'Размер рыбы: {self._size}'


class Birds(Animal):

    def __init__(self, kind, name, age, color):
        super().__init__(kind, name, age)
        self._color = color

    def get_specific(self):
        return f'Окрас птицы: {self._color}'


class Mammals(Animal):

    def __init__(self, kind, name, age, spec):
        super().__init__(kind, name, age)
        self._spec = spec

    def get_specific(self):
        return f'Особенность животного: {self._spec}'

if __name__ == '__main__':
    f1 = Fishes('Карась', 'Федя', 1, 15)
    b1 = Birds('Галка', 'Хватайка', 1, 'черный')
    m1 = Mammals('Кот', 'Матроскин', 8, 'говорящий кот')
    list_animals = [f1, b1, m1]

    for animal in list_animals:
        print(animal.get_kind())
        print(animal.get_name())
        print(animal.get_age())
        print(animal.get_specific())

# print(f'Вид: {f1.get_kind()}')
# print(f'кличка: {f1.get_name()}')
# print(f'возраст: {f1.get_age()} лет')
# print(f'размер: {f1.get_specific()} см.')
