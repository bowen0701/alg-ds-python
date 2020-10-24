"""Palindrome: a string that read the same forward and backward.

For example: radar, madam.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def palindrom_reverse(s):
    """Check palindrome by inverse slicing.

    Time complexity: O(n).
    Space complexity: O(n).
    """
    return s == s[::-1]


def palindrom_recur(s):
    """Check palindrome by recursion.

    Time complexity: O(n^2).
    Space complexity: O(n).
    """
    if len(s) <= 1:
        return True
    else: 
        return s[0] == s[-1] and palindrom_recur(s[1:-1])


def palindrome_iter(s):
    """Check palindrom by left & right match.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    ls = list(s)

    # Apply two pointer method.
    left = 0
    right = len(ls) - 1

    while left < right:
        l = ls[left]
        r = ls[right]

        if l != r:
            return False

        left += 1
        right -= 1

    return True


def main():
    import time

    start_time = time.time()
    s = 'madam'
    print('{0}: {1}'.format(s, palindrom_reverse(s)))    
    s = 'Bowen'
    print('{0}: {1}'.format(s, palindrom_reverse(s)))
    s = 'toot'
    print('{0}: {1}'.format(s, palindrom_reverse(s)))
    print('Time for palindrom_reverse(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    s = 'madam'
    print('{0}: {1}'.format(s, palindrome_iter(s))) 
    s = 'Bowen'
    print('{0}: {1}'.format(s, palindrome_iter(s)))
    s = 'toot'
    print('{0}: {1}'.format(s, palindrome_iter(s)))
    print('Time for palindrome_iter(): {}'
          .format(time.time() - start_time))

    start_time = time.time()
    s = 'madam'
    print('{0}: {1}'.format(s, palindrom_recur(s)))    
    s = 'Bowen'
    print('{0}: {1}'.format(s, palindrom_recur(s)))
    s = 'toot'
    print('{0}: {1}'.format(s, palindrom_recur(s)))
    print('Time for palindrom_recur(): {}'
          .format(time.time() - start_time))


if __name__ == '__main__':
    main()
