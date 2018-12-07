"""Palindrome: a string that read the same forward and backward.

For example: radar, madam.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def palindrome(a_str):
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


def palindrom_recur(a_str):
    """Check palindrome by recursion."""
    if len(a_str) <= 1:
        return True
    else: 
        return a_str[0] == a_str[-1] and palindrom_recur(a_str[1:-1])


def main():
    import time

    start_time = time.time()
    a_str = 'madam'
    print('{0}: {1}'.format(a_str, palindrome(a_str))) 
    a_str = 'Bowen'
    print('{0}: {1}'.format(a_str, palindrome(a_str)))
    a_str = 'toot'
    print('{0}: {1}'.format(a_str, palindrome(a_str)))
    print('Time for palindrome(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    a_str = 'madam'
    print('{0}: {1}'.format(a_str, palindrom_recur(a_str)))    
    a_str = 'Bowen'
    print('{0}: {1}'.format(a_str, palindrom_recur(a_str)))
    a_str = 'toot'
    print('{0}: {1}'.format(a_str, palindrom_recur(a_str)))
    print('Time for palindrom_recur(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
