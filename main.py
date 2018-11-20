"""Project Frontend"""
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


if __name__ == '__main__':
    main()
