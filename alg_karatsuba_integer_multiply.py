from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math


def karatsuba_integer_multiply(x, y):
    """Multiply 2 n-digits integers by Karatsuba's algorithm.

    This is a divide-and-conquer algorithm.
  
    We would like to multiply two long n-bits integers (of maybe not equal 
    length), where
      x = x_L * 10^(n/2) + x_R
      y = y_L * 10^(n/2) + y_R
    Since
      xy = x_L y_L 10^n + (x_L y_R + x_R y_L) 10^(n/2) + x_R y_R
         = x_L y_L 10^n
           + [(x_L + x_R)((y_L + y_R) - x_L y_L - x_R y_R] 10^(n/2)
           + x_R y_R

    Time complexity: O((n + n)^log3) = O(n^1.59), 
    much faster than the naive one with O(n^2).
    """
    n_x = int(math.log10(x))
    n_y = int(math.log10(y))

    if n_x <= 1 or n_y <= 1:
        return x * y

    # Since x and y may be not of equal size, take smaller size.
    n = min(n_x, n_y)

    # Split x and number in the middle.
    x_l, x_r = divmod(x, 10 ** (n // 2))
    y_l, y_r = divmod(y, 10 ** (n // 2))
    
    xy_l = karatsuba_integer_multiply(x_l, y_l)
    xy_sum = karatsuba_integer_multiply(x_l + x_r, y_l + y_r)
    xy_r = karatsuba_integer_multiply(x_r, y_r)

    return (xy_l * (10 ** n)
            + (xy_sum - xy_l - xy_r) * (10 ** (n // 2))
            + xy_r)


def main():
    x = 1
    y = 1234
    print('(x, y): ({}, {})'.format(x, y))
    print('Multiply: {}'.format(karatsuba_integer_multiply(x, y)))

    x = 12
    y = 12345
    print('(x, y): ({}, {})'.format(x, y))
    print('Multiply: {}'.format(karatsuba_integer_multiply(x, y)))


if __name__ == '__main__':
    main()
