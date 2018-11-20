"""Unit Tests for specialized algorithms"""
from collections import deque
from unittest import TestCase
import unittest

from src.algorithms import opt


class TestAlgorithms(TestCase):
    """Test opt algorithm"""
    def setUp(self):
        self.page_table = deque((2, 4, 7, 6, 5))

    def test_perfect_victim(self):
        """Test opt algorithm"""
        expected = deque((2, 4, 7, 6))
        ref_string = deque((3, 2, 4, 7, 6))

        opt(self.page_table, ref_string)
        self.assertEqual(expected, self.page_table)

    def test_regular(self):
        """test opt algo under regular conditions"""
        expected = deque((2, 4, 6, 5))
        ref_string = deque((13, 56, 4, 67, 2, 5, 6, 7, 54, 3))

        opt(self.page_table, ref_string)
        self.assertEqual(expected, self.page_table)


if __name__ == '__main__':
    unittest.main()
