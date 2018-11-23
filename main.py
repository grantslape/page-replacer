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
    args = parser.parse_args()

    seed = args.seed if args.seed else sf['PRNG_SEED']
    np.random.seed(seed)
    ref_string = generate_ref_string(
        length=sf['REF_STRING_SIZE'],
        max_page=sf['MAX_VIRTUAL_PAGE']
    )

    prefix = utcnow().timestamp
    results = run(ref_string)
    plot_path = plot_results(results, prefix)
    file_path = write_csv(results, prefix)

    print('Plot path is at; {}'.format(plot_path))
    print('CSV path is at: {}'.format(file_path))


def run(ref_string: deque) -> [dict]:
    """
    Run the full suite of simulations
    :param ref_string: Ref string to use for all simulations
    :return: list of dict of results
    """
    results = []
    for key, schedule_type in SCHEDULE_TYPES.items():
        for i in range(sf['MAX_PHYS_PAGE']):
            results.append(Simulator(schedule_type, i + 1, ref_string).run_once())

    return results


if __name__ == '__main__':
    main()
