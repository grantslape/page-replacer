"""Shared functions"""
from collections import deque
import numpy as np


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


def index(collection: list, target: int) -> int:
    """
    return first index target is at, throw value error if not found
    This is functionally the same as the deque.index() method that was added
    in Python 3.5 - for <3.4 compatibility this is used instead.
    :param collection: collection to search
    :param target: target to search for
    :return: index of item
    """
    for idx, item in enumerate(collection):
        if item == target:
            return idx

    raise ValueError('Not Found')
