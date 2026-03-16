smallest_number(numbers

from unittest import TestCase

import list_function


class TestClass(TestCase):

    def test_smallest_number(self):
        numbers = [5, 3, 8, 2, 9]
        result = find_smallest(numbers)
        self.assertEqual(result, 2)

    def test_smallest_with_negative_numbers(self):
        numbers = [-4, -1, -7, -3]
        result = find_smallest(numbers)
        self.assertEqual(result, -7)

    def test_single_number(self):
        numbers = [10]
        result = find_smallest(numbers)
        self.assertEqual(result, 10)

