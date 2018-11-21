"""Simulation methods"""
from collections import deque

from src.algorithms import opt
from src.commons.settings import settings as sf
from src.commons.settings import TYPES as SCHEDULE_TYPES
from src.commons.commons import generate_ref_string, index


class Simulator:
    """
    Simulator class
    """
    def __init__(self, schedule_type: int, table_size: int, ref_string: deque = None):
        if schedule_type not in SCHEDULE_TYPES.values():
            raise ValueError('Unknown schedule type')

        self.schedule_type = schedule_type
        self.page_table = deque(maxlen=table_size)
        if ref_string is None:
            self.ref_string = generate_ref_string(
                length=sf['REF_STRING_SIZE'],
                max_page=sf['MAX_VIRTUAL_PAGE']
            )
        else:
            self.ref_string = deque(ref_string)

    def run_once(self) -> dict:
        """
        Run the simulation once
        :return: dict of simulation results
        """
        faults = 0

        while self.ref_string:
            next_val = self.ref_string.popleft()
            try:
                index(list(self.page_table), next_val)
            except ValueError:
                # NOT FOUND, page fault
                faults += 1
                if len(self.page_table) == self.page_table.maxlen:
                    self.replace(next_val)
                else:
                    self.page_table.append(next_val)
            else:
                self.found(next_val)

        return {
            'type': self.schedule_type,
            'max_frames': self.page_table.maxlen,
            'page_faults': faults
        }

    def found(self, value: int):
        """
        Found item handler
        :param value: value that was found
        :return:
        """
        if self.schedule_type == SCHEDULE_TYPES['LRU']:
            self.page_table.remove(value)
            self.page_table.append(value)

    def replace(self, next_val):
        """Page replacement handler"""
        if self.schedule_type == SCHEDULE_TYPES['FIFO'] or \
                self.schedule_type == SCHEDULE_TYPES['LRU']:
            self.page_table.popleft()
        elif self.schedule_type == SCHEDULE_TYPES['OPT']:
            opt(self.page_table, self.ref_string)
        else:
            raise KeyError(
                'Schedule Type not found: {}'.format(self.schedule_type)
            )

        self.page_table.append(next_val)
