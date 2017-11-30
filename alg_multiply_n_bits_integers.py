from __future__ import absolute_import
from __future__ import division
from __future__ import print_function 

def multiply_n_bits_integers(x, y):
    """Multiply 2 n-bits integers by divide-and-conquer algorithm.
  
    We would like to multiply two long n-bits integers, where
      x = 2^(n/2) x_L + x_R
      y = 2^(n/2) y_L + y_R
    Since
      xy = 2^n x_L y_L + 2^(n/2) (x_L y_R + x_R y_L) + x_R y_R
         = 2^n x_L y_L 
           + 2^(n/2) [(x_L + x_R)((y_L + y_R) - x_L y_L - x_R y_R] 
           + x_R y_R
    The divide-and-conquer algorithm using the 2nd equality would
    result in much faster runtime O(n^1.59) 
    compared with using the 1st one with O(n^2).
    """
    if len(x) != len(y):
        raise ValueError('The 2 integers are not of equal length.')
    else:
        n = len(x) - 2
    # TODO: Get bit length by bit_length().
    # x_L, x_R = int(x[:(n // 2)]), int(y[(n // 2):])
    # y_L, y_R = int(x[:(n // 2)]), int(y[(n // 2):])
    print('x_L, x_R: {}, {}'.format(x_L, x_R))
    print('y_L, y_R: {}, {}'.format(y_L, y_R))
    mul_L = x_L * y_L
    mul_R = x_R * y_R
    sum_mul = (x_L + x_R) * (y_L + y_R)
    mul = (
        mul_L * 10^n 
        + (sum_mul - mul_L - mul_R) * 10^(n // 2)
        + mul_R)
    return mul


def main():
    # x = 1234
    # y = 123
    # print('(x, y): ({}, {})'.format(x, y))
    # print(multiply_two_ints(x, y))

    x = 1234
    y = 1234
    print('(x, y): ({}, {})'.format(x, y))
    print(multiply_two_ints(x, y))

    x = 12345
    y = 12345
    print('(x, y): ({}, {})'.format(x, y))
    print(multiply_two_ints(x, y))

if __name__ == '__main__':
    main()
