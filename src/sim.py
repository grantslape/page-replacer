"""Simulation methods"""
from collections import deque
import numpy as np

from src.commons.settings import settings as sf
from src.commons.settings import TYPES as SCHEDULE_TYPES


class Simulator:
    """
    Simulator class
    """
    def __init__(self, schedule_type: int, table_size: int):
        if schedule_type not in SCHEDULE_TYPES:
            raise ValueError('Unknown schedule type')

        self.schedule_type = schedule_type
        self.page_table = deque(maxlen=table_size)
        self.ref_string = self.generate_ref_string(
            length=sf['REF_STRING_SIZE'],
            max_page=sf['MAX_VIRTUAL_PAGE']
        )

    @staticmethod
    def generate_ref_string(length: int, max_page: int) -> deque:
        """
        Generate reference string to use for test
        :param length: length of page reference string to generate
        :param max_page: max page number to use
        :return: Queue representing reference string
        """
        return deque(
            np.random.randint(
                low=0,
                high=max_page,
                size=length
            ),
            maxlen=length
        )

    def run_once(self) -> dict:
        """
        Run the simulation once
        :return: dict of simulation results
        """
        faults = 0

        while len(self.ref_string) > 0:
            next_val = self.ref_string.popleft()
            try:
                self.page_table.index(next_val)
            except ValueError as Ex:
                # NOT FOUND, page fault
                faults += 1
            else:
                self.found(next_val)

        return {}

    def found(self, value: int):
        """
        Found item handler
        :param value: value that was found
        :return:
        """
        if self.schedule_type == SCHEDULE_TYPES['LRU']:
            self.page_table.remove(value)
            self.page_table.append(value)
