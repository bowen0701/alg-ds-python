from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

digits = '0123456789ABCDEF'


def decimal_to_base2(decimal):
    """Convert decimal number to binary number."""
    rem_stack = []
    while decimal > 0:
        decimal, rem = divmod(decimal, 2)
        rem_stack.append(rem)

    bin_num = ''
    while rem_stack:
        bin_num += str(rem_stack.pop())
    return bin_num


def decimal_to_base_iter(decimal, base):
    """Convert decimal number to base 2 ~ 16.

    Time complexity: O(d/b).
    Space complexity: O(d/b).
    """
    rem_stack = []
    while decimal > 0:
        decimal, rem = divmod(decimal, base)
        rem_stack.append(rem)

    base_num = ''
    while rem_stack:
        base_num += digits[rem_stack.pop()]
    return base_num


def _decimal_to_base_recur(decimal, base, rem_stack):
    if decimal < base:
        rem_stack.append(decimal)
    else:
        decimal, rem = divmod(decimal, base)
        rem_stack.append(rem)
        _decimal_to_base_recur(decimal, base, rem_stack)


def decimal_to_base_recur(decimal, base):
    """Convert decimal number to base 2 ~ 16 by recussion with Stack.

    Time complexity: O(d/b).
    Space complexity: O(d/b).
    """
    rem_stack = []
    _decimal_to_base_recur(decimal, base, rem_stack)

    base_num = ''
    while rem_stack:
        base_num += digits[rem_stack.pop()]
    return base_num


def main():
    # Binary: (37)_10 = (100101)_2
    decimal = 37
    print('Iter: {} -> {}'
          .format(decimal, decimal_to_base2(decimal)))
    print('Iter: {} -> {}'
          .format(decimal, decimal_to_base_iter(decimal, 2)))

    # Hexadecimal: (1728)_10 = (6C0)_16
    decimal = 1728
    print('Iter: {} -> {}'
          .format(decimal, decimal_to_base_iter(decimal, 16)))
    print('Recur: {} -> {}'
          .format(decimal, decimal_to_base_recur(decimal, 16)))


if __name__ == '__main__':
    main()
