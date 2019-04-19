from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

digits = '0123456789ABCDEF'


def decimal_to_base2(dec_num):
    """Convert decimal number to binary number."""
    rem_stack = []
    while dec_num > 0:
        dec_num, rem = divmod(dec_num, 2)
        rem_stack.append(rem)

    bin_str = ''
    while rem_stack:
        bin_str += str(rem_stack.pop())
    return bin_str


def decimal_to_base_iter(dec_num, base):
    """Convert decimal number to base 2 ~ 16."""
    rem_stack = []
    while dec_num > 0:
        dec_num, rem = divmod(dec_num, base)
        rem_stack.append(rem)

    bin_str = ''
    while rem_stack:
        bin_str += digits[rem_stack.pop()]
    return bin_str


def _decimal_to_base_recur(dec_num, base, rem_stack):
    if dec_num < base:
        rem_stack.append(dec_num)
    else:
        dec_num, rem = divmod(dec_num, base)
        rem_stack.append(rem)
        _decimal_to_base_recur(dec_num, base, rem_stack)


def decimal_to_base_recur(dec_num, base):
    """Convert decimal number to base 2 ~ 16 by recussion with Stack."""
    rem_stack = []
    _decimal_to_base_recur(dec_num, base, rem_stack)

    bin_str = ''
    while rem_stack:
        bin_str += digits[rem_stack.pop()]
    return bin_str


def main():
    # Binary: (37)_10 = (100101)_2
    dec_num = 37
    print('Convert {} to binary: {}'
          .format(dec_num, decimal_to_base2(dec_num)))
    print('Convert {} to binary: {}'
          .format(dec_num, decimal_to_base_iter(dec_num, 2)))

    # Hexadecimal: (1728)_10 = (6C0)_16
    dec_num = 1728
    print('Convert {} to hexadecimal: {}'
          .format(dec_num, decimal_to_base_iter(dec_num, 16)))
    print('Convert {} to hexadecimal: {}'
          .format(dec_num, decimal_to_base_recur(dec_num, 16)))


if __name__ == '__main__':
    main()
