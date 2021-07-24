"""Sample random variable."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import random
import itertools


class SampleUniformDiscrete(object):
    def __init__(self, vals):
        """Sample uniform discrete values.

        Apply the Probability Integral Transform for uniform discrete r.v.,
          [x_0, ..., x_{n-1}] with probs 1/n:
        X = int(n*U), where U ~ Uniform(0, 1).

        Args:
          vals: A list. Values from which we want to sample.

        Time complexity: O(1).
        Space complexity: O(n), where n is the number of input values.
        """
        self.n = len(vals)
        self.vals = vals

    def sample(self):
        """Sample values in uniform probabilities.

        Time complexity: O(1).
        Space complexity: O(n).
        """
        # Sample a r.v. from Uniform(0, 1).
        u = random.uniform(0, 1)
        i = int(self.n * u)
        return self.vals[i]


class SampleNonUniformDiscrete(object):
    def __init__(self, vals, probs, n_bins=int(1e4)):
        """Sampling non-uniform discrete numbers.

        For r.v.'s with non-uniform probs, preprocess to "uniform" r.v.
        See https://www.keithschwarz.com/darts-dice-coins/
        - Specifically, preprocess [x_0, x_1, ...] with [p_0, p_1, ...] to
          repeated values [x_0, x_0, x_1, x_1, ...] with frequencies proportional to probs.
        - Apply the Probability Integral Transform for uniform discrete r.v.'s,
          [x_0, ..., x_m] with probs 1/m, where m = number of total repeated values:
          X = int(m*U), where U ~ Uniform(0, 1).

        Args:
          vals: A list. Values from which we want to sample.
          probs: A list. Sampling probabilities for values. Default: None.
          n_bins: A int. Bin number to duplicate values for uniform r.v. Default: 1000.
        """
        # Simulate non-uniform values by uniform values
        self.vals = vals
        self.probs = probs
        self.n_bins = n_bins
        self.is_constructed = False

    def construct(self):
        """Construct repeated values based probabilites for "uniform" r.v.
        
        Time complexity: O(nb),
          - n: number of values.
          - b: number of bins.
        Space complexity: O(nb).
        """
        # Construct only for the 1st call.
        if self.is_constructed:
            return None;

        # Construct repeated values with corresponding binned freqs.
        binned_freqs = [int(round(self.n_bins * p)) for p in self.probs]
        binned_vals_ls = [[v] * f for v, f in zip(self.vals, binned_freqs)]
        binned_vals = [v for ls in binned_vals_ls for v in ls]

        self.is_constructed = True
        self.n = len(binned_vals)
        self.binned_vals = binned_vals

    def sample(self):
        """Sample non-uniform values with "uniform" probabilities.

        Time complexity: O(1) for infinite calls.
        Space complexity: O(nb).
        """
        self.construct()

        # Sample a r.v. from Uniform(0, 1).
        u = random.uniform(0, 1)
        i = int(self.n * u)
        return self.binned_vals[i]


class SampleBiasedCoinWithFairCoin(object):
    def __init__(self, p):
        """Smple biased coin with p = 1/k by fair coin.

        First compute the number of fair coins we need to flip.
          n_cases = 1/p
          2^n_coins = n_cases => n_coins = ceiling(log2(n_cases))

        Note: This function only applies to rational p = 1/k.
        """
        if 1 / p != int(1 / p):
            raise ValueError("p must be an rational number 1 / k.")

        self.n_cases = int(1 / p)
        self.n_coins = int(math.ceil(math.log(self.n_cases, 2)))

        # Iterate the possible results of flipping coins.
        self.possible_flips = list(itertools.product([0, 1], repeat=self.n_coins))

    def sample(self):
        """Sample biased coin.

        First flip number of coins, if the flipped coins is 
        - the first case in possible flips, return success;
        - the (last) n_cases - 1 case, return failures;
        - the rest cases, retry.
        """
        # Convert to tuple due to tuples in itertools's product ouput.
        flips = tuple([random.randint(0, 1) for _ in range(self.n_coins)])

        # Use only the 1st case and the last (n_cases - 1) as sampling basis.
        if flips == self.possible_flips[0]:
            return 1
        elif flips in set(self.possible_flips[-(self.n_cases-1):]):
            return 0
        else:
            return self.sample()


class SampleFairCoinWithBiasedCoin(object):
    def __init__(self, p):
        """Smple fair coin with biased coin having head probility p."""
        self.p = p

    def _sample_biased(self):
        """Sample with biased coin."""
        u = random.uniform(0, 1)
        if u <= self.p:
            return 1
        else:
            return 0

    def sample(self):
        """Sample fair coin with biased coin.

        Note: For biased coin with head H probability p < 1/2,
        - The probability of (H, T): p*(1-p)
        - The probability of (T, H): (1-p)*p = that of (H, T).
        Thus we obtain "fair" probibilities for these two cases.
        For the rest cases, retry.
        """
        # Flip two biased coins.
        two_flips = [self._sample_biased() for _ in range(2)]

        # Use cases (1, 0) and (0, 1) for fair coin flipping.
        if two_flips == [1, 0]:
            return 1
        elif two_flips == [0, 1]:
            return 0
        else:
            return self.sample()


def main():
    import numpy as np

    n_exp = int(1e5)

    # Sample discrete random variable with equal probs.
    # Output: should be close to 0.5
    vals = [0, 1]
    sample_discrete = SampleUniformDiscrete(vals)

    samples = [None] * n_exp
    for i in range(n_exp):
        samples[i] = sample_discrete.sample()
    print(np.mean(samples))

    # Sample discrete random variable with unequal probs.
    # Output: should be close to 0.7
    vals = [0, 1, 2]
    probs = [0.5, 0.3, 0.2]
    sample_discrete = SampleNonUniformDiscrete(vals, probs)

    samples = [None] * n_exp
    for i in range(n_exp):
        samples[i] = sample_discrete.sample()
    print(np.mean(samples))

    # Sample biased coin with fair one.
    # Output: should be close to 1/4 = 0.25.
    p = 1 / 4
    sample_biased_coin = SampleBiasedCoinWithFairCoin(p)

    samples = [None] * n_exp
    for i in range(n_exp):
        samples[i] = sample_biased_coin.sample()
    print(np.mean(samples))

    # Sample fair coin with biased one.
    # Output: should be close to 0.5.
    p = 1 / 4
    sample_fair_coin = SampleFairCoinWithBiasedCoin(p)

    samples = [None] * n_exp
    for i in range(n_exp):
        samples[i] = sample_fair_coin.sample()
    print(np.mean(samples))


if __name__ == '__main__':
    main()
