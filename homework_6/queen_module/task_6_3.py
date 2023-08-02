"""Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки"""

from random import randint
from queen_move import battle_queens

def arrangement_queens(combinations: int):
    """Выводит успешныe расстановки ферзей на доске."""
    while combinations > 0:
        pos = list((i, randint(1, 9)) for i in range(1, 9))
        if battle_queens(pos):
            print(pos)
            combinations -= 1


if __name__ == "__main__":
    arrangement_queens(1)


