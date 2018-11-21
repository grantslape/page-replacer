"""Unit tests for Sim helper functions"""
from collections import deque
from unittest import TestCase
import unittest

from src.commons.settings import TYPES as SCHEDULE_TYPES
from src.sim import Simulator


class TestSimulator(TestCase):
    """Test Simulation"""
    def test_found(self):
        """Test Found handler for LRU"""
        sim = Simulator(SCHEDULE_TYPES['LRU'], 5)
        sim.page_table = deque((2, 5, 6, 8), maxlen=5)
        expected = deque((2, 6, 8, 5), maxlen=5)

        sim.found(5)
        self.assertEqual(expected, sim.page_table)


class TestReplace(TestCase):
    """Test replace for different types"""
    def setUp(self):
        self.sut = Simulator(SCHEDULE_TYPES['FIFO'], 5)
        self.sut.page_table = deque((2, 5, 6, 8, 7), maxlen=5)
        self.expected = deque((5, 6, 8, 7))

    def test_fifo(self):
        """Test FIFO replacement"""
        self.sut.replace()
        self.assertEqual(self.expected, self.sut.page_table)

    def test_lru(self):
        """Test LRU replacement"""
        self.sut.schedule_type = SCHEDULE_TYPES['LRU']
        self.sut.replace()
        self.assertEqual(self.expected, self.sut.page_table)


if __name__ == '__main__':
    unittest.main()
