#import unittest 
from unittest import TestCase
class TestClass(TestCase):
#ClassTestClass(unittest.TestCase):
    def test_number_is_prime(self):
        self.assertTrue(True)
#python3 -m unittest test_functionpy
#prime_number = 11
    is_prime = number_is_prime (11)
    self.assertTrue(is_prime)

def number_is_prime(number):
    factor = 0
    counter = 2
    while(counter<number):
        if (number % counter == 0):
            factors += 1
            counter += 1
    if (factors == 0):
        return True
    return False
