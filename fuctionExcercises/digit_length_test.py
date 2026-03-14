from unittest import TestCase

import digit_length

class digit_length_test(TestCase):

    def test_that_first_number_is_negative(self):
   
        is_negative_number = first_number_is_negative (-1, 25)
        actual_number = 0

        self.assertEqual(is_negative_number, actual_number)
#
#
#    def test_that_second_number_is_between_two_and_thirtysix(self):
#        second_number = 7
#        result = second_number_is_between_two_and_thirtysix(second_number)
#
#        self.assertTrue(result)
#
#    def test_that_second_number_is_not_out_of_range(self):
#        second_number = 45
#        result = second_number_is_not_out_of_range(second_number)
#
#        self.assertFalse(result) 
#
#    def test_that_parameters_takes_in_two_integers(self):
#        first_number = 0
#        second_number = 0
#        result = parameters_takes_in_two_integers(first_number, second_number)
#
#        self.assertTrue(result)
#
#    def test_that_seond_number_is_divisible_by_the_double_of_the_first_numbervbnb(self):
#        pass
