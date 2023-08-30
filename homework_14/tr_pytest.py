import pytest
from triangle import Triangle


def test_init():
    """Проверка равенства (и создания экземпляра)"""
    assert Triangle(6, 7, 3) == Triangle(6, 7, 3)


def test_err():
    """Стороны треугольника должны быть положительными"""
    with pytest.raises(AttributeError):
        Triangle(5, 4, -2)


def test_square():
    """Проверка нахождения площади треугольника"""
    triangle_1 = Triangle(5, 4, 6)
    assert triangle_1.square() == 9.92


def test_disparity():
    """Проверка неравенства"""
    assert Triangle(6, 5, 4) != Triangle(5, 4, 7)


def test_equality():
    """Проверка равенства"""
    assert Triangle(6, 5, 4) == Triangle(5, 4, 6)


if __name__ == '__main__':
    pytest.main(['-v'])
