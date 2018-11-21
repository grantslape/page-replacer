"""Project Frontend"""
import numpy as np
import argparse
from collections import deque
from arrow import utcnow

from commons.commons import generate_ref_string
from modeller import plot_results
from sim import Simulator
from src.commons.settings import settings as sf
from src.commons.settings import TYPES as SCHEDULE_TYPES


def main():
    """Main program execution"""
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
    plot_results(results, prefix)


def run(ref_string: deque) -> [dict]:
    """"""
    results = []
    for key, schedule_type in SCHEDULE_TYPES.items():
        for i in range(sf['MAX_PHYS_PAGE']):
            results.append(Simulator(schedule_type, i + 1, ref_string).run_once())

    return results


if __name__ == '__main__':
    main()
