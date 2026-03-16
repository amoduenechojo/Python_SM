from unittest import TestCase

import list_function


class TestClass(TestCase):

    def test_that_the_length_of_list_is_up_to_more_than_three_indexs(self):
        numbers = [12, 45, 89]

        expectedLength  = 4
        actualLength = adding_third_elements(numbers)

        self.assertEquals(actualLength, expectedLength)
        

    def test_that_the_summation_of_the_thurs_indexes_is_correct(self):        

        result = adding_third_elements(8, 5, 4, 5, 3, 56)
        self.assertEqual(result, 60)
































adding_third_elements
