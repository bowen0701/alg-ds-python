from __future__ import print_function
from ds_stack import Stack


def convert_decimal_to_base2(dec_num):
    """Convert decimal number to binary number."""
    rem_stack = Stack()
    
    while dec_num > 0:
        rem = dec_num % 2
        rem_stack.push(rem)
        dec_num = dec_num // 2

    bin_str = ''
    while not rem_stack.is_empty():
        bin_str = bin_str + str(rem_stack.pop())

    return bin_str


def convert_decimal_to_base(dec_num, base):
    """Convert decimal number to any base."""
    rem_stack = Stack()

    digits = '0123456789ABCDEF'

    while dec_num > 0:
        rem = dec_num % base
        rem_stack.push(rem)
        dec_num = dec_num // base

    bin_str = ''
    while not rem_stack.is_empty():
        bin_str = bin_str + digits[rem_stack.pop()]

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


if __name__ == '__main__':
    main()
