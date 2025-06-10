import unittest
from main import sum_two


class TestSumTwo(unittest.TestCase):

    def test_correct_values(self):
        self.assertEqual(sum_two(1, 2), 3)
        self.assertEqual(sum_two(a=5, b=10), 15)

    def test_incorrect_values_float(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

    def test_incorrect_values_str(self):
        with self.assertRaises(TypeError):
            sum_two(1, '2')

    def test_incorrect_values_bool(self):
        with self.assertRaises(TypeError):
            sum_two(1, True)

    def test_three_values(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2, 3)

