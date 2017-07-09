"""Palindrome: a string that read the same forward and backward.

For example: radar, madam.
"""

from __future__ import print_function
from __future__ import division

import numpy as np


def match_palindrome(a_str):
    """Check palindrom by front & rear match by Deque."""
    from ds_deque import Deque

    str_deque = Deque()

    for s in a_str:
        str_deque.add_rear(s)

    still_match = True

    while str_deque.size() > 1 and still_match:
        first = str_deque.remove_front()
        last = str_deque.remove_rear()
        if first != last:
            still_match = False
    
    return still_match


def main():
    a_str = 'madam'
    print('{0}: {1}'.format(a_str, match_palindrome(a_str)))
    
    a_str = 'Bowen'
    print('{0}: {1}'.format(a_str, match_palindrome(a_str)))

    a_str = 'toot'
    print('{0}: {1}'.format(a_str, match_palindrome(a_str)))


if __name__ == '__main__':
    main()
