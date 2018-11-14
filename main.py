"""Project Frontend"""
from src.commons.settings import settings as sf
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
    table = np.zeros_like(np.arange(table_size))



if __name__ == '__main__':
    main()
