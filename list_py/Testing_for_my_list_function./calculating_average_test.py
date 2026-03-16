from unittest import TestCase

import list_function


class TestClass(TestCase):

    def test_the_average_of_positive_numbers(self):
        positive_numbers = [1, 23, 56, 10]

        result = calculate_average(numbers)
        self.assertEqual(result, 22.5)

    def test_the_average_of_negative_numbers(self):
        negative_numbers = [-23, -45, -10, -5]

        result = calculate_average(numbers)
        self.assertEqual(result, -20.75)

    def test_the_average_of_two_numbers(self):
        double_numbers = [800, 18]

        result = calculate_average(numbers)
        self.assertEqual(result, 409)
