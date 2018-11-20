"""Simulation methods"""
from queue import Queue
import numpy as np

from src.commons.settings import settings as sf


def generate_ref_string(length: int, max_page: int) -> Queue:
    """
    Generate reference string to use for test
    :param length: length of page reference string to generate
    :param max_page: max page number to use
    :return: Queue representing reference string
    """
    response = Queue(maxsize=length)
    while not response.full():
        response.put(np.random.randint(max_page))

    return response


def search(collection: Queue, target: int) -> int:
    """
    Search collection for target item
    :param collection: collection to search
    :param target: target of search
    :return: index of item, -1 if not found
    """
    for index, item in enumerate(collection.queue):
        if item == target:
            return index

    return -1


def run_once(size: int) -> dict:
    """
    Run the simulation once
    :param size:
    :return: dict of simulation results
    """
    ref_string = generate_ref_string(
        length=sf['REF_STRING_SIZE'],
        max_page=size
    )

    while not ref_string.empty():
        next_val = ref_string.get()
        if search(ref_string, next_val):
            # TODO: USED HANDLER
            pass
        else:
            pass


    return {}
