"""Random Variate Generator for exponential distribution."""

import math
import random
import matplotlib.pyplot as plt


def rvg_exp(lam : float = 1) -> float:
    """Return a random variate from an exponential distribution with
    parameter lam.
    :param lam: Lambda parameter of the exponential distribution.
    :return: A random variate from the exponential distribution.
    """
    return -math.log(1 - random.random())/lam


def plot_rvg_exp(n : int, lam : float = 1, bins : int = 100) -> None:
    """Plot a histogram of n random variates from an exponential
    distribution with parameter lam.
    :param n: Number of random variates to generate.
    :param lam: Lambda parameter of the exponential distribution.
    :param bins: Number of bins in the histogram.
    """
    data = [rvg_exp(lam) for i in range(n)]
    plt.hist(data, bins=bins)
    plt.ylabel('Sample Count')
    plt.xlabel('Random Variate')
    plt.show()
    
if __name__ == "__main__":
    plot_rvg_exp(10)
    plot_rvg_exp(100)
    plot_rvg_exp(1000)
    plot_rvg_exp(100000)