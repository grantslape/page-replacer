"""Unit Tests for aux functions in main"""
from unittest import TestCase
import unittest
import numpy as np

from src.commons.settings import settings as sf
from src.sim import Simulator


class TestAux(TestCase):
    """Unit Tests for aux functions in main"""
    def setUp(self):
        np.random.seed(sf['PRNG_SEED'])

    def test_generate(self):
        """Test reference string generation"""
        for _ in range(sf['TEST_LENGTH']):
            self._generate()

    def _generate(self):
        """test runner for generate"""
        ref_string = Simulator.generate_ref_string(
            length=sf['REF_STRING_SIZE'],
            max_page=sf['MAX_VIRTUAL_PAGE']
        )

        while len(ref_string) > 0:
            value = ref_string.popleft()
            self.assertTrue(0 <= value <= sf['MAX_VIRTUAL_PAGE'])


if __name__ == '__main__':
    unittest.main()
