from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

DIGITS = '0123456789ABCDEF'


def decimal_to_base2(decimal):
    """Convert decimal number to binary number by iteration.

    Time complexity: O(d/2).
    Space complexity: O(d/2).
    """
    # Push remainders into stack.
    rem_stack = []
    while decimal > 0:
        decimal, rem = divmod(decimal, 2)
        rem_stack.append(rem)

    # Pop remainders and concat them into binary number string.
    bin_num = ''
    while rem_stack:
        bin_num += str(rem_stack.pop())
    return bin_num


def decimal_to_base_iter(decimal, base):
    """Convert decimal number to base 2 ~ 16 by iteration.

    Time complexity: O(d/b).
    Space complexity: O(d/b).
    """
    # Push remainders into stack.
    rem_stack = []
    while decimal > 0:
        decimal, rem = divmod(decimal, base)
        rem_stack.append(rem)

    # Pop remainders and concat them into base number string.
    base_num = ''
    while rem_stack:
        base_num += DIGITS[rem_stack.pop()]
    return base_num


def _decimal_to_base_recur_util(decimal, base, rem_stack):
    # 
    if decimal < base:
        rem_stack.append(decimal)
    else:
        decimal, rem = divmod(decimal, base)
        rem_stack.append(rem)
        _decimal_to_base_recur_util(decimal, base, rem_stack)


def decimal_to_base_recur(decimal, base):
    """Convert decimal number to base 2 ~ 16 by recursion with stack.

    Time complexity: O(d/b).
    Space complexity: O(d/b).
    """
    # Push remainders into stack.
    rem_stack = []
    _decimal_to_base_recur_util(decimal, base, rem_stack)

    # Pop remainders and concat them into base number string.
    base_num = ''
    while rem_stack:
        base_num += DIGITS[rem_stack.pop()]
    return base_num


def main():
    import time

    # Binary: (37)_10 = (100101)_2
    decimal = 37

    start_time = time.time()
    print('By iter w/ base 2: {} -> {}'
          .format(decimal, decimal_to_base2(decimal)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter w/ general base 2: {} -> {}'
          .format(decimal, decimal_to_base_iter(decimal, 2)))
    print('Time: {}'.format(time.time() - start_time))

    # Hexadecimal: (1728)_10 = (6C0)_16
    decimal = 1728

    start_time = time.time()
    print('By iter: {} -> {}'
          .format(decimal, decimal_to_base_iter(decimal, 16)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By recur: {} -> {}'
          .format(decimal, decimal_to_base_recur(decimal, 16)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
