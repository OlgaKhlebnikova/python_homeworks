from triangle import Triangle
import unittest


class TestTriangle(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(str(Triangle(5, 4, 6)), 'Треугольник со сторонами: (5, 4, 6)')


    def test_side(self):
        self.assertRaises(AttributeError, Triangle, 5, 4, -2)



    def test_square(self):
        self.assertEqual(Triangle(5, 4, 6).square(), 9.92)

    def test_comparison(self):
        self.assertEqual(Triangle(5, 4, 6) == Triangle(6, 5, 4), True)
        self.assertEqual(Triangle(5, 4, 6) == Triangle(5, 4, 7), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)