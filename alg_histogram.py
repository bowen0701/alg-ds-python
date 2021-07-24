from __future__ import absolute_import, division, print_function


class Histogram(object):
    def __init__(self, x, n_bins):
        """Histogram with bin counters.

        Args:
          x: A list. Numbers to calculate histogram.
          n_bins: An int. Number of bins.

        Returns:
          bin_vals: A list. Values for bins.
          bin_counters: A list. Counters for bins.
        """
        x_min = min(x)
        x_max = max(x)
        x_range = x_max - x_min

        # Compute bin size.
        bin_size = x_range / n_bins

        # Set bin values which are bins's lower bounds.
        bin_vals = [x_min + bin_size * b for b in range(n_bins)]

        bin_counters = [0] * n_bins
        for x_ in x:
            if x_ != x_max:
                b = int((x_ - x_min) // bin_size)
            else:
                b = int(n_bins - 1)
            bin_counters[b] += 1

        self.x_min = x_min
        self.x_max = x_max
        self.n_bins = n_bins
        self.bin_size = bin_size
        self.bin_vals = bin_vals
        self.bin_counters = bin_counters


def main():
    x = range(100)
    n_bins = 8
    histogram = Histogram(x, n_bins)
    print(histogram.n_bins)
    print(histogram.bin_size)
    print(histogram.bin_vals)
    print(histogram.bin_counters)


if __name__ == '__main__':
    main()
