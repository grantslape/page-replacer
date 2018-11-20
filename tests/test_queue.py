"""Unit Tests for page queue"""
import unittest
from unittest import TestCase
import numpy as np

from collections import deque
from src.commons.settings import settings as sf


class TestQueue(TestCase):
    """Unit Tests for page queue"""
    def setUp(self):
        np.random.seed(sf['PRNG_SEED'])

    def test_shift_middle(self):
        """Test shift() when value is in the middle"""
        sut = deque((2, 45, 67, 5, 23), maxlen=5)

        for value in given:
            sut.put(value)

        self.assertTrue(sut.full())

        sut.shift(2)

        self.assertTrue(not sut.full())

        for value in expected:
            self.assertEqual(value, sut.get())


if __name__ == '__main__':
    unittest.main()
