"""Palindrome: a string that read the same forward and backward.

For example: radar, madam.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def palindrome_iter(a_str):
    """Check palindrom by left & right match.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    ls = list(a_str)

    # Apply two pointer method.
    left = 0
    right = len(ls) - 1

    while right - left >= 2:
        l = ls[left]
        r = ls[right]
        if l != r:
            return False

        left += 1
        right -= 1

    return True


def palindrom_recur(a_str):
    """Check palindrome by recursion.

    Time complexity: O(n^2).
    Space complexity: O(n).
    """
    if len(a_str) <= 1:
        return True
    else: 
        return a_str[0] == a_str[-1] and palindrom_recur(a_str[1:-1])


def palindrom_reverse(a_str):
    """Check palindrome by inverse slicing.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    return a_str == a_str[::-1]


def main():
    import time

    start_time = time.time()
    a_str = 'madam'
    print('{0}: {1}'.format(a_str, palindrome_iter(a_str))) 
    a_str = 'Bowen'
    print('{0}: {1}'.format(a_str, palindrome_iter(a_str)))
    a_str = 'toot'
    print('{0}: {1}'.format(a_str, palindrome_iter(a_str)))
    print('Time for palindrome_iter(): {}'
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
    print('{0}: {1}'.format(a_str, palindrom_reverse(a_str)))    
    a_str = 'Bowen'
    print('{0}: {1}'.format(a_str, palindrom_reverse(a_str)))
    a_str = 'toot'
    print('{0}: {1}'.format(a_str, palindrom_reverse(a_str)))
    print('Time for palindrom_reverse(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
