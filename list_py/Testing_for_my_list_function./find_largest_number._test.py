from unittest import TestCase

import list_function


class TestClass(TestCase):

    def test_that_largest_number_can_be_seen(self):
        number = [12, 67, 89]

        expectedNumber = 67

        actualNumber = find_largest_number(number)
        self.assertEqual(actualNumber, expectedNumber)

    def test_that_the_number_is_the_largest_number(self):
        number = [89, 12, 67]

        expectedNumber = 67

        actualNumber = find_largest_number(number)
        self.assertEqual(actualNumber, expectedNumber)
