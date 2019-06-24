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
    l2 = list(s2)

    pos1 = 0
    is_match = True

    while pos1 < len(s1) and is_match:
        pos2 = 0
        is_found = False

        while pos2 < len(l2) and not is_found:
            if s1[pos1] == s2[pos2]:
                is_found = True
            else:
                pos2 += 1

        if is_found:
            l2[pos2] = None
        else:
            is_match = False
            break

        pos1 += 1

    return is_match 


def anagram_sort(s1, s2):
    """Anagram by sorting.

    Time complexity: O(nlogn).
    Space complexity: O(n).
    """
    l1 = list(s1)
    l2 = list(s2)

    l1.sort()
    l2.sort()
    
    pos = 0
    is_match = True
    
    while pos < len(s1) and is_match:
        if l1[pos] == l2[pos]:
            pos += 1
        else:
            is_match = False
            break
    
    return is_match


def anagram_count(s1, s2):
    """Anagram by counting.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    
    pos = 0
    is_match = True
    
    while pos < 26 and is_match:
        if c1[pos] == c2[pos]:
            pos += 1
        else:
            is_match = False
            break
    
    return is_match


def main():
    import time

    s1 = 'abcd'
    s2 = 'dcba'

    start_time = time.time()
    print('By anagram_iter(): {}'.format(anagram_iter(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By anagram_sort(): {}'.format(anagram_sort(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By anagram_count(): {}'.format(anagram_count(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    s1 = 'abcd'
    s2 = 'aabc'

    start_time = time.time()
    print('By anagram_iter(): {}'.format(anagram_iter(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By anagram_sort(): {}'.format(anagram_sort(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By anagram_count(): {}'.format(anagram_count(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
