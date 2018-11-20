import numpy as np
import unittest
from queue import Queue, PriorityQueue
from unittest import TestCase

from src.commons.settings import settings as sf
from main import generate_ref_string, search


class TestAux(TestCase):
    """Unit Tests for aux functions in main"""
    def testSearch(self):
        """Test Search function"""
        for _ in range(sf['TEST_LENGTH']):
            self._search()

    def testGenerate(self):
        """Test reference string generation"""
        for _ in range(sf['TEST_LENGTH']):
            self._generate()

    def _generate(self):
        """test runner for generate"""
        ref_string = generate_ref_string(
            length=sf['REF_STRING_SIZE'],
            max_page=sf['MAX_VIRTUAL_PAGE']
        )

        while not ref_string.empty():
            value = ref_string.get()
            self.assertTrue(0 <= value <= sf['MAX_VIRTUAL_PAGE'])

    def _search(self):
        """test runner for search"""
        shuffled_queue = PriorityQueue(maxsize=sf['MAX_PHYS_PAGE'])
        queue = Queue(maxsize=sf['MAX_PHYS_PAGE'])
        target = None

        while not shuffled_queue.full():
            number = np.random.randint(sf['MAX_VIRTUAL_PAGE'])
            if target is None:
                target = number
            # Shuffle the generated numbers
            shuffled_queue.put((np.random.randint(10000), number))

        while not shuffled_queue.empty():
            queue.put(shuffled_queue.get()[1])

        self.assertTrue(search(queue, target))


if __name__ == '__main__':
    unittest.main()
