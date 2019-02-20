from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

digits = '0123456789ABCDEF'


def convert_decimal_to_base2(dec_num):
    """Convert decimal number to binary number."""
    rem_stack = []
    
    while dec_num > 0:
        dec_num, rem = divmod(dec_num, 2)
        rem_stack.append(rem)

    bin_str = ''

    while rem_stack:
        bin_str += str(rem_stack.pop())

    return bin_str


def convert_decimal_to_base(dec_num, base):
    """Convert decimal number to any base."""
    rem_stack = []

    while dec_num > 0:
        dec_num, rem = divmod(dec_num, base)
        rem_stack.append(rem)

    bin_str = ''

    while rem_stack:
        bin_str += digits[rem_stack.pop()]

    return bin_str


def _recur_decimal_to_base(dec_num, base, rem_stack):
    if dec_num < base:
        rem_stack.append(digits[dec_num])
    else:
        dec_num, rem = divmod(dec_num, base)
        rem_stack.append(digits[rem])
        _recur_decimal_to_base(dec_num, base, rem_stack)
    
    return None


def convert_decimal_to_base_recur(dec_num, base):
    """Convert decimal number to any base by recussion with Stack."""
    rem_stack = []
    _recur_decimal_to_base(dec_num, base, rem_stack)
    bin_str = ''
    while rem_stack:
        bin_str += rem_stack.pop()
    return bin_str


def main():
    dec_num = 1024
    print('Convert {} to base 2: {}'
          .format(dec_num, convert_decimal_to_base2(dec_num)))

    dec_num = 233
    print('Convert {} to base 2: {}'
          .format(dec_num, convert_decimal_to_base2(dec_num)))
    print('Convert {} to base 8: {}'
          .format(dec_num, convert_decimal_to_base(dec_num, 8)))
    print('Convert {} to base 16: {}'
          .format(dec_num, convert_decimal_to_base(dec_num, 16)))

    print('Convert {} to base 16: {}'
          .format(dec_num, convert_decimal_to_base_recur(dec_num, 16)))


if __name__ == '__main__':
    main()
