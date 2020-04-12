import sys
sys.path.insert(0, '../')
from fibonacci import *
from unittest import TestCase

my_object = Find_fibonacci()

class FibonacciTestCase(TestCase):
    def setUp(self):
        self.fibonacci_test_data = [
            [1, 1], [2, 1], [3, 2], [4, 3],
            [5, 5], [6, 8], [7, 13], [8, 21],
            [9, 34], [10, 55], [11, 89], [12, 144]
        ]

    def test_fibonacci_test_data(self):
        for n, expected_number in self.fibonacci_test_data:
            actual_number = my_object.find_fibonacci(n)
            self.assertEqual(expected_number, actual_number)

    def test_first_fibonacci_number_is_1(self):
        x = my_object.find_fibonacci(1)
        self.assertEqual(1, x)

    def test_second_fibonacci_number_is_1(self):
        x = my_object.find_fibonacci(2)
        self.assertEqual(1, x)

    def test_second_fibonacci_number_is_5(self):
        x = my_object.find_fibonacci(5)
        self.assertEqual(5, x)
    