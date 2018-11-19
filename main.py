"""Project Frontend"""
from queue import Queue

from src.commons.settings import settings as sf
from src.commons.settings import TYPES as SCHEDULE_TYPES
import numpy as np
import argparse


def main():
    """Main program execution"""
    parser = argparse.ArgumentParser()
    parser.add_argument('seed', type=int, help='Base seed for PRNG')
    args = parser.parse_args()


def run(table_size: int):
    """

    :param table_size:
    :return:
    """
    for key, value in SCHEDULE_TYPES:
        for max_page in sf['MAX_PHYS_PAGE']:
            table = np.zeros_like(np.arange(table_size))
            pass


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


def search(collection: Queue, target: int) -> bool:
    """
    Search collection for target item
    :param collection: collection to search
    :param target: target of search
    :return: True if found, False if not
    """
    for item in collection.queue:
        if item == target:
            return True

    return False


if __name__ == '__main__':
    main()
