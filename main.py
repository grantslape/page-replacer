"""Project Frontend"""
from collections import deque
import argparse

import numpy as np
from arrow import utcnow

from src.modeller import plot_results, write_csv
from src.sim import Simulator
from src.commons.commons import generate_ref_string
from src.commons.settings import settings as sf
from src.commons.settings import TYPES as SCHEDULE_TYPES


def main():
    """
    Main program execution
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('seed', type=int, help='Base seed for PRNG')
    parser.add_argument(
        '-p', '--pages',
        type=int,
        required=False,
        help='Max number of physical page frames to simulate'
    )
    parser.add_argument(
        '--virtual-pages',
        type=int,
        required=False,
        help='Maximum virtual page number to use starting at 0'
    )
    parser.add_argument(
        '-r', '--ref-string',
        type=int,
        required=False,
        help='Size of reference string to use'
    )
    args = parser.parse_args()

    seed = args.seed if args.seed else sf['PRNG_SEED']
    max_pages = args.pages if args.pages else sf['MAX_PHYS_PAGE']
    virtual_pages = args.virtual_pages if args.virtual_pages else sf['MAX_VIRTUAL_PAGE']
    string_size = args.ref_string if args.ref_string else sf['REF_STRING_SIZE']

    np.random.seed(seed)
    ref_string = generate_ref_string(
        length=string_size,
        max_page=virtual_pages
    )
    prefix = utcnow().timestamp

    results = run(ref_string, max_pages)

    plot_path = plot_results(results, prefix)
    file_path = write_csv(results, prefix)

    print('Plot path is at; {}'.format(plot_path))
    print('CSV path is at: {}'.format(file_path))


def run(ref_string: deque, max_pages: int) -> [dict]:
    """
    Run the full suite of simulations
    :param ref_string: Ref string to use for all simulations
    :param max_pages: max number of pages to use
    :return: list of dict of results
    """
    results = []
    for key, schedule_type in SCHEDULE_TYPES.items():
        for i in range(max_pages):
            results.append(Simulator(schedule_type, i + 1, ref_string).run_once())

    return results


if __name__ == '__main__':
    main()
