from queen_move import battle_queens
from task_6_2 import check_battle
from task_6_3 import arrangement_queens

arrangement_queens(4)
position = (1, 6), (2, 4), (3, 2), (4, 8), (5, 5), (6, 7), (7, 1), (8, 3)
position_2 = (1, 6), (2, 3), (3, 6), (4, 9), (5, 2), (6, 8), (7, 1), (8, 4)
check_battle(position)
check_battle(position_2)
