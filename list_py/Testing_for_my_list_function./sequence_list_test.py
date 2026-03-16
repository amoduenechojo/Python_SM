import unittest
from list_function

class TestSequenceList(TestCase):

    def test_sequence_list_returns_same_list(self):
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        result = sequence_list(numbers)

        self.assertEqual(result, numbers)

