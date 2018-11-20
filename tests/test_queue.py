"""Unit Tests for page queue"""
import unittest
from unittest import TestCase
import numpy as np

from src.commons.settings import settings as sf


class TestQueue(TestCase):
    """Unit Tests for page queue"""
    def setUp(self):
        np.random.seed(sf['PRNG_SEED'])


if __name__ == '__main__':
    unittest.main()
