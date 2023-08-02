def battle_queens(position: list) -> bool:
    """Определяет, есть ли среди ферзей пара бьющих друг друга."""
    n = 8
    x = []
    y = []

    for i in range(n):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True

    else:
        return False


if __name__ == "__main__":
    position_1 = (1, 3), (2, 6), (4, 1), (7, 7), (5, 8), (8, 2), (3, 4), (6, 5)
    print(battle_queens(position_1))
    position_2 = (1, 4), (2, 6), (4, 1), (7, 7), (5, 8), (8, 2), (3, 4), (6, 5)
    print(battle_queens(position_2))
