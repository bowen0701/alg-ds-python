from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math


def multiply_n_digits_integers(x, y):
    """Multiply 2 n-bits integers by divide-and-conquer algorithm.
  
    We would like to multiply two long n-bits integers, where
      x = x_L * 10^(n/2) + x_R
      y = y_L * 10^(n/2) + y_R
    Since
      xy = 2^n x_L y_L + 2^(n/2) (x_L y_R + x_R y_L) + x_R y_R
         = 2^n x_L y_L 
           + 2^(n/2) [(x_L + x_R)((y_L + y_R) - x_L y_L - x_R y_R] 
           + x_R y_R

    The divide-and-conquer algorithm using the 2nd equality would
    result in much faster runtime O(n^1.59) 
    compared with using the 1st one with O(n^2).
    """
    x_n = int(math.log10(x)) + 1
    y_n = int(math.log10(y)) + 1
    if x_n != y_n:
        raise ValueError('The 2 integers are not of equal length.')
    else:
        n = x_n
    x_L, x_R = divmod(x, 10 ** (n // 2))
    y_L, y_R = divmod(y, 10 ** (n // 2))
    mul_L = x_L * y_L
    mul_R = x_R * y_R
    sum_mul = (x_L + x_R) * (y_L + y_R)
    mul = (
        mul_L * (10 ** ((n // 2) * 2))
        + (sum_mul - mul_L - mul_R) * (10 ** (n // 2))
        + mul_R)
    return mul


def main():
    x = 1234
    y = 1234
    print('(x, y): ({}, {})'.format(x, y))
    print('Multiply: {}'.format(multiply_n_digits_integers(x, y)))

    x = 12345
    y = 12345
    print('(x, y): ({}, {})'.format(x, y))
    print('Multiply: {}'.format(multiply_n_digits_integers(x, y)))

if __name__ == '__main__':
    main()
