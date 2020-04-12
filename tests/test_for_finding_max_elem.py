import sys
sys.path.insert(0, '../')
from find_max_element import *
from unittest import TestCase

my_object = Find_max_elem()

class FindMaxElemTestCase(TestCase):
    def setUp(self):
        self.max_elem_test_data = [
            [[1,2,3,4,5,6], 6], [[4,-5,1,54,-78], 54], [[5,90,-40,3,8,9,0], 90],
            [[7,9,3,-1,9], 9], [[2,76,45,32,100,122], 122]
        ]