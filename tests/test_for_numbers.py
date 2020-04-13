import sys
sys.path.insert(0, '../')
from numbers import *
from unittest import TestCase

my_object = Numbers()

class NumbersTestCase(TestCase):
    def setUp(self):
        self.return_list_test_data = [
            [1,9, [1,2,3,4,5,6,7,8,9]], [-5,5, [-5,-4,-3,-2,-1,0,1,2,3,4,5]], [80,85, [80,81,82,83,84,85]],
            [8,10, [8,9,10]], [100,104, [100,101,102,103,104]], [-1,4, [-1,0,1,2,3,4]]
        ]

    def test_return_list_test_data(self):
        for a, b, expected_list in self.return_list_test_data:
            actual_list = my_object.return_list(a, b)
            self.assertListEqual(expected_list, actual_list)

    def test_first_list_test(self):
        x = my_object.return_list(0,5)
        self.assertListEqual([0,1,2,3,4,5], x)

    def test_second_list_test(self):
        x = my_object.return_list(-40,-35)
        self.assertListEqual([-40,-39,-38,-37,-36,-35], x)

   