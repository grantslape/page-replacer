"""Simulation methods"""
from collections import deque
import numpy as np

from src.commons.settings import settings as sf


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


def run_once(size: int) -> dict:
    """
    Run the simulation once
    :param size: max physical page
    :return: dict of simulation results
    """
    ref_string = generate_ref_string(
        length=sf['REF_STRING_SIZE'],
        max_page=size
    )

    page_table = deque(maxlen=size)

    while len(ref_string) > 0:
        next_val = ref_string.popleft()
        try:
            index = page_table.index(next_val)
        except ValueError as Ex:
            # NOT FOUND
            pass
        else:
            # FOUND
            # TODO Used handler w/ index
            pass

    return {}
