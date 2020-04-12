import sys
sys.path.insert(0, '../')
from find_max_element import *
from unittest import TestCase

my_object = Find_max_elem()

class FindMaxElemTestCase(TestCase):
    def setUp(self):
        self.max_elem_test_data = [
            [[1,2,3,4,5,6], 6], [[4,-5,1,54,-78], 54], [[5,90,-40,3,8,9,0], 90],
            [[7,9,3,-1,9], 9], [[2,76,45,32,100,122], 122], [[1,7,6,4,1,1,1,9], 9]
        ]

    def test_max_elem_test_data(self):
        for my_list, expected_number in self.max_elem_test_data:
            actual_number = my_object.find_max_elem(my_list)
            self.assertEqual(expected_number, actual_number)

    def test_first_fibonacci_number_is_10(self):
        x = my_object.find_max_elem([1,2,3,-2,-9,10])
        self.assertEqual(10, x)

    def test_first_fibonacci_number_is_100(self):
        x = my_object.find_max_elem([1,20,32,-23,-90,100])
        self.assertEqual(100, x)

    def test_first_fibonacci_number_is_89(self):
        x = my_object.find_max_elem([-1,-90,-32,-23,89,88])
        self.assertEqual(89, x)