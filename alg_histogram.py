from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def histogram(x_ls, num_bins):
    """Histogram with bin counters.

    Args:
      x_ls: A list. Numbers to calculate histogram.
      num_bins: An int. Number of bins.

    Returns:
      bin_counters_ls: A list. Counters for bins.
    """
    x_min = min(x_ls)
    x_max = max(x_ls)
    x_range = x_max - x_min
    bin_size = x_range / num_bins
    bin_counters_ls = [0 for _ in range(num_bins)]
    for x in x_ls:
        if x != x_max:
            b = int((x - x_min) // bin_size)
        else:
            b = int(num_bins - 1)
        bin_counters_ls[b] += 1
    return bin_counters_ls
    

def main():
    x_ls = range(100)
    num_bins = 8
    bin_counters_ls = histogram(x_ls, num_bins)
    print(bin_counters_ls)

if __name__ == '__main__':
    main()
