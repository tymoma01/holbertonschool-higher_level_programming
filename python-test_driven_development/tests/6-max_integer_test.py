#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -9, -3, -10]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 5, 3, -1]), 5)

    def test_all_same_number(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 2, 3.1]), 3.1)

    def test_string(self):
        self.assertEqual(max_integer("abcxyz"), "z")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "pear"]), "pear")


if __name__ == "__main__":
    unittest.main()
