"""Sample random variable."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math
import random
import itertools


class SampleUniformDiscrete(object):
    def __init__(self, values):
        """Sample uniform discrete values.

        Apply the Probability Integral Transform for uniform discrete r.v.,
          [x_1, ..., x_n] with probs 1/n:
        X = int(n*U) + 1, where U ~ Uniform(0, 1).

        Args:
          values: A list. Values from which we want to sample.
        """
        self.n = len(values)
        self.values = values

    def sample(self):
        """Sample from values with probs."""
        # Sample a r.v. from Uniform(0, 1).
        u = random.uniform(0, 1)

        # Get index = int(n*u) since index starts from 0.
        i = int(self.n * u)
        return self.values[i]


class SampleNonUniformDiscrete(object):
    def __init__(self, values, probs, n_bins=1000):
        """Sampling non-uniform discrete numbers.

        - For r.v.'s with unequal probs, preprocess to "uniform" r.v. with uniform probabilies.
          Specifically, preprocess [x_1, x_2, ...] with [p_1, p_2, ...] to
          duplicated values [x_1, x_1, ..., x_2, x_2, ...] with frequencies based on probs.
        - Then apply the Probability Integral Transform for uniform discrete r.v.'s,
          [x_1, ..., x_m] with probs 1/m:
          X = int(m*U) + 1, where U ~ Uniform(0, 1).

        Args:
          values: A list. Values from which we want to sample.
          probs: A list. Sampling probabilities for values. Default: None.
          n_bins: A int. Bin number to duplicate values for uniform r.v. Default: 1000.
        """
        self.n_bins = n_bins

        # Duplicate values by the corresponding binned freqs.
        binned_freqs = [int(round(self.n_bins * p)) for p in probs]
        binned_values_ls = [[v] * f for v, f in zip(values, binned_freqs)]
        binned_values = [v for ls in binned_values_ls for v in ls]

        self.n = len(binned_values)
        self.values = binned_values

    def sample(self):
        """Sample from values with probs."""
        # Sample a r.v. from Uniform(0, 1).
        u = random.uniform(0, 1)

        # Get index = int(n*u) since index starts from 0.
        i = int(self.n * u)
        return self.values[i]


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

    n_sim = 10000

    # Sample discrete random variable with equal probs.
    # Output: should be close to 0.5
    values = [0, 1]
    sample_discrete = SampleUniformDiscrete(values)

    samples = [None] * n_sim
    for i in range(n_sim):
        samples[i] = sample_discrete.sample()
    print(np.mean(samples))

    # Sample discrete random variable with unequal probs.
    # Output: should be close to 0.7
    values = [0, 1, 2]
    probs = [0.5, 0.3, 0.2]
    sample_discrete = SampleNonUniformDiscrete(values, probs)

    samples = [None] * n_sim
    for i in range(n_sim):
        samples[i] = sample_discrete.sample()
    print(np.mean(samples))

    # Sample biased coin with fair one.
    # Output: should be close to 1/4 = 0.25.
    p = 1 / 4
    sample_biased_coin = SampleBiasedCoinWithFairCoin(p)

    samples = [None] * n_sim
    for i in range(n_sim):
        samples[i] = sample_biased_coin.sample()
    print(np.mean(samples))

    # Sample fair coin with biased one.
    # Output: should be close to 0.5.
    p = 1 / 4
    sample_fair_coin = SampleFairCoinWithBiasedCoin(p)

    samples = [None] * n_sim
    for i in range(n_sim):
        samples[i] = sample_fair_coin.sample()
    print(np.mean(samples))


if __name__ == '__main__':
    main()
