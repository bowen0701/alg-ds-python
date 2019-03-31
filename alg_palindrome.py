"""Palindrome: a string that read the same forward and backward.

For example: radar, madam.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def palindrome(a_str):
    """Check palindrom by front & rear match."""
    ls = list(a_str)

    is_match = True

    while len(ls) > 1 and is_match:
        first = ls.pop(0)
        last = ls.pop()
        if first != last:
            is_match = False
    
    return is_match


def palindrom_recur(a_str):
    """Check palindrome by recursion."""
    if len(a_str) <= 1:
        return True
    else: 
        return a_str[0] == a_str[-1] and palindrom_recur(a_str[1:-1])


def palindrom(a_str):
    """Check palindrome by inverse slicing."""
    return a_str == a_str[::-1]


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

    start_time = time.time()
    a_str = 'madam'
    print('{0}: {1}'.format(a_str, palindrom(a_str)))    
    a_str = 'Bowen'
    print('{0}: {1}'.format(a_str, palindrom(a_str)))
    a_str = 'toot'
    print('{0}: {1}'.format(a_str, palindrom(a_str)))
    print('Time for palindrom(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
