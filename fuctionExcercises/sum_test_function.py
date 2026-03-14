from unittest import TestCase
import sum_of_numbers

class TestClass(TestCase):

    def test_that_function_takes_two_numbers(self):
        
        expected = sum_of_numbers.get_sum_of_two_numbers(5,6);
        actual = 5+6
        self.assertEqual(expected, actual)

    def test_that_function_returns_sum_of_two_numbers(self):
        
        expected = sum_of_numbers.get_sum_of_two_numbers(5,6);
        actual = 11
        self.assertEqual(expected, actual)
    
    def test_that_function_returns_sum_of_two_negtive_numbers(self):
        
        expected = sum_of_numbers.get_sum_of_two_numbers(-5,-6);
        actual = -11
        self.assertEqual(expected, actual)

    def test_that_function_returns_sum_of_a_negtive_and_positive_numbers(self):
        
        expected = sum_of_numbers.get_sum_of_two_numbers(-5,6);
        actual = 1
        self.assertEqual(expected, actual)

    def test_that_function_returns_sum_of_decimal_numbers(self):
        
        expected = sum_of_numbers.get_sum_of_two_numbers(-5.5,6.0);
        actual = -5.5 + 6.0
        self.assertEqual(expected, actual)

        

    def test_that_function_returns_0_when_first_number_is_a_character(self):
        
        expected = sum_of_numbers.get_sum_of_two_numbers("a",6);
        actual = 0
        self.assertEqual(expected, actual)

    def test_that_function_returns_0_when_second_number_is_a_character(self):
        
        expected = sum_of_numbers.get_sum_of_two_numbers(5,"a");
        actual = 0
        self.assertEqual(expected, actual)
            

    
