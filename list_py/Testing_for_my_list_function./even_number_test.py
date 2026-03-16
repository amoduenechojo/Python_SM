from unittest import TestCase

import list_function


class TestClass(TestCase):
    def test_for_the_sum_of_even_numbers(self):
        even_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        result = even_numbers(numbers)
        self.assertEqual(result, 18)

    def test_that_the_even_numbers_don't_give_reminders_when_divided(self):
        numbers = [98]

        result = even_numbers(numbers)
        self.assertEquals(result, 49)

