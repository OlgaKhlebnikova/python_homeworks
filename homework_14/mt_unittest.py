import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(str(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) + Matrix([[10, 9, 8], [8, 7, 6], [6, 5, 4]])), '[11, 11, 11]\n[12, 12, 12]\n[13, 13, 13]\n')

    def test_mul(self):
        self.assertEqual(str(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) * Matrix([[10, 9, 8], [8, 7, 6], [6, 5, 4]])), '[44, 38, 32]\n[116, 101, 86]\n[188, 164, 140]\n')

    def test_comparison(self):
        self.assertEqual(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == Matrix([[3, 2, 3], [6, 5, 6], [9, 8, 9]]), False)

    def test_side(self):
        with self.assertRaises(ValueError):
            Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == Matrix([[3, 2, 3, 6], [6, 5, 6, 5], [9, 8, 9, 2]])
if __name__ == '__main__':
    unittest.main(verbosity=2)