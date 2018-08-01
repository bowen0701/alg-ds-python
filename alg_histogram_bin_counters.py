from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def get_histogram_bin_counters(x_ls, num_bins):
    """Histogram bin counters.

    Args:
      x_ls: A list. Numbers to calculate histogram.
      num_bins: An int. Number of bins.

    Returns:
      bin_counters_ls: A list. Counters for bins.
    """
    if not isinstance(x_ls, list):
        raise TypeError('x_ls is expected to be a list.')
    if not isinstance(num_bins, int):
        raise TypeError('num_bins is expected to be an int.')

    x_min = min(x_ls)
    x_max = max(x_ls)
    x_range = x_max - x_min
    bin_size = x_range / num_bins
    bin_counters_ls = [0 for _ in range(num_bins)]
    for x in x_ls:
        if x != x_max:
            b = (x - x_min) // bin_size
        else:
            b = num_bins - 1
        bin_counters_ls[int(b)] += 1
    return bin_counters_ls
    

def main():
    x_ls = range(100)
    num_bins = 8
    bin_counters_ls = get_histogram_bin_counters(x_ls, num_bins)
    print('x_ls = range(100)')
    print('num_bins: {}'.format(num_bins))
    print(bin_counters_ls)

if __name__ == '__main__':
    main()
