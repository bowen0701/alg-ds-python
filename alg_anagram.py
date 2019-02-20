"""Anagram detecting problem.

Two strings are anagram if one is simply a rearrangement of the other.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def anagram_iter(s1, s2):
    """Anagram by iteration."""
    l2 = list(s2)

    pos1 = 0
    match_bool = True

    while pos1 < len(s1) and match_bool:
        pos2 = 0
        found = False

        while pos2 < len(l2) and not found:
            if s1[pos1] == l2[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            l2[pos2] = None
        else:
            match_bool = False
            break

        pos1 += 1

    return match_bool 


def anagram_sort(s1, s2):
    """Anagram by sorting."""
    l1 = list(s1)
    l2 = list(s2)

    l1.sort()
    l2.sort()
    
    pos = 0
    match_bool = True
    
    while pos < len(s1) and match_bool:
        if l1[pos] == l2[pos]:
            pos += 1
        else:
            match_bool = False
            break
    
    return match_bool


def anagram_count(s1, s2):
    """Anagram by counting."""
    c1 = [0] * 26
    c2 = [0] * 26
    
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1
    
    j = 0
    match_bool = True
    
    while j < 26 and match_bool:
        if c1[j] == c2[j]:
            j += 1
        else:
            match_bool = False
            break
    
    return match_bool


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
