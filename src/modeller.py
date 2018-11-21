from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def write_csv(results: [dict]) -> Path:
    """
    Write results to CSV
    :param results: list of dicts, dict for each row
    :return: Path to output csv
    """
    return Path()


def plot_results(results: [dict]) -> Path:
    """
    Plot results
    :param results: list of dicts, dict for each row
    :return: Path to generated plot
    """
    data = pd.DataFrame(results)
    data = data.sort_values(['type', 'max_frames'])

    print(data)

    fig, ax = plt.subplots()

    for key, group in data.groupby(['type']):
        group.plot(ax=ax, marker='o', x='max_frames', y='page_faults', label=key)

    ax.set_title('Page Faults')
    ax.set_xlabel('Max physical frames')
    ax.set_ylabel('Page faults')
    ax.grid(True)

    fig.tight_layout()
    plt.savefig('ax')

    return Path()
