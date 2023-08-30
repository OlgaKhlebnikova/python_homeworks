from matrix import *
import pytest


def test_sum():
    """Проверка сложения"""
    assert str(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) + Matrix(
        [[10, 9, 8], [8, 7, 6], [6, 5, 4]])), '[11, 11, 11]\n[12, 12, 12]\n[13, 13, 13]\n'

def test_mul():
    """Проверка произведение двух матриц"""
    assert str(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) * Matrix(
        [[10, 9, 8], [8, 7, 6], [6, 5, 4]])) == '[44, 38, 32]\n[116, 101, 86]\n[188, 164, 140]\n'
def test_type():
    """Проверка ошибки"""
    with pytest.raises(ValueError):
        Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == Matrix([[3, 2, 3, 5], [6, 5, 6, 8], [9, 8, 9, 6]])

def test_disparity():
    """Проверка неравенства"""
    assert Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) != Matrix([[3, 2, 3], [6, 5, 6], [9, 8, 9]])



if __name__ == '__main__':
    pytest.main(['-v'])
