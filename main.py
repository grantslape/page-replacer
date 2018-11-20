"""Project Frontend"""
from sim import Simulator
from src.commons.settings import settings as sf
from src.commons.settings import TYPES as SCHEDULE_TYPES
import numpy as np
import argparse


def main():
    """Main program execution"""
    parser = argparse.ArgumentParser()
    parser.add_argument('seed', type=int, help='Base seed for PRNG')
    args = parser.parse_args()

    seed = args.seed if args.seed else sf['PRNG_SEED']
    np.random.seed(seed)

    results = run()
    print(results)


def run() -> [dict]:
    """"""
    results = []
    for schedule_type in SCHEDULE_TYPES:
        for i in range(sf['MAX_PHYS_PAGE']):
            results.append(Simulator(schedule_type, i).run_once())

    return results


if __name__ == '__main__':
    main()
