"""Modelling functions"""
import csv
from os import rename
from pathlib import Path

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


BASE_PATH = 'data'


def write_csv(results: [dict], prefix: str) -> Path:
    """
    Write results to CSV
    :param results: list of dicts, dict for each row
    :param prefix: file prefix for saved results
    :return: Path to output csv
    """
    identifier = '{}/{}.csv'.format(BASE_PATH, prefix)

    with open(identifier, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(rowdicts=results)

    return Path(identifier)


def plot_results(results: [dict], prefix: str) -> Path:
    """
    Plot results
    :param results: list of dicts, dict for each row
    :param prefix: file prefix for saved image
    :return: Path to generated plot
    """
    data = pd.DataFrame(results)
    data = data.sort_values(['type', 'max_frames'])

    fig, ax = plt.subplots()

    for key, group in data.groupby(['type']):
        group.plot(ax=ax, marker='o', x='max_frames', y='page_faults', label=key)

    ax.set_title('Page Faults')
    ax.set_xlabel('Max physical frames')
    ax.set_ylabel('Page faults')
    ax.grid(True)

    fig.tight_layout()
    plt.savefig('ax')
    identifier = '{}/{}_plot.png'.format(BASE_PATH, prefix)
    rename('ax.png', identifier)

    return Path(identifier)
