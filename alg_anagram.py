"""Anagram detecting problem.

Two strings are anagram if one is simply a rearrangement of the other.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def anagram_iter(s1, s2):
    """Anagram by iteration.

    Time complexity: O(n^2).
    Space complexity: O(n).
    """
    if len(s1) != len(s2):
        return False

    # Make list of s2 for search memoization.  
    l2 = list(s2)

    for c1 in s1:
        is_found = False
        for i2, c2 in enumerate(s2):
            if c2 == c1:
                # If c1 is found as a char c2 in s2, 
                # update its l2 for not duplicating search.
                l2[i2] = None
                is_found = True
                break

        # Confirm c1 is found in any char of s2.
        if is_found:
            continue
        else:
            return False

    return True


def anagram_sort(s1, s2):
    """Anagram by sorting.

    Time complexity: O(nlogn).
    Space complexity: O(n).
    """
    if len(s1) != len(s2):
        return False

    # Sort lists of s1 and s2.
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            continue
        else:
            return False

    return True


def anagram_count(s1, s2):
    """Anagram by counting.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    if len(s1) != len(s2):
        return False

    # Use 26 chars from a to z to store s1/s2's char numbers.
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    
    for i in range(26):
        if c1[i] == c2[i]:
            continue
        else:
            return False

    return True


def main():
    import time

    # Output: True.
    s1 = 'abcd'
    s2 = 'dcba'

    start_time = time.time()
    print('By iter: {}'.format(anagram_iter(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By sort: {}'.format(anagram_sort(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By count: {}'.format(anagram_count(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    # Output: False.
    # s1 = 'abcd'
    # s2 = 'aabc'
    s1 = 'abcd'
    s2 = 'abc'

    start_time = time.time()
    print('By iter: {}'.format(anagram_iter(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By sort: {}'.format(anagram_sort(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By count: {}'.format(anagram_count(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
