"""Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""
from animals import Fishes, Birds, Mammals


class AnimalFabric:
    def record_animal(self, animal_kind, *args, **kwargs):
        new_animal = self._get_animal_key(animal_kind)
        return new_animal(*args, **kwargs)

    def _get_animal_key(self, animal_kind: str):
        kinds = {"рыба": Fishes, "птица": Birds, "млекопитающие": Mammals}
        return kinds[animal_kind]


if __name__ == '__main__':
    fabric = AnimalFabric()
    fab_an_1 = fabric.record_animal("рыба", "гуппи", "Петя", 1, 3)
    fab_an_2 = fabric.record_animal("птица", "ворона", "Каркуша", 10, 'черный')
    fab_an_3 = fabric.record_animal("млекопитающие", "собака", "Шарик", 11, 'спаниель')
    list_animals = [fab_an_1, fab_an_2, fab_an_3]

    for animal in list_animals:
        print(animal.get_kind())
        print(animal.get_name())
        print(animal.get_age())
        print(animal.get_specific())
