"""Binomial Cofficients

Binomial Coefficient of m taking k, 
C(m, k) = m!(m - k)!/k!
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def binomial_cofficient(m, k):
    """Binomial coefficien of m taking k.

    Note there is a recursion relationship:
    C(m, k) = C(m - 1, k - 1) + C(m - 1, k)
    which represents C(m, k) is the sum of choosing and not choosing item m.
    """
    pass


def main():
    pass


if __name__ == '__main__':
    main()
