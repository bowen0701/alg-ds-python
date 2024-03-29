from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _lcs_recur(s1, s2, n1, n2):
    """Helper function for longest_common_subsequence_recur()."""
    if n1 == 0 or n2 == 0:  # Base case.
        return 0
    
    if s1[n1 - 1] == s2[n2 - 1]:
        # If the current chars are the same, LCS is the last LCS plus 1.
        result = _lcs_recur(s1, s2, n1 - 1, n2 - 1) + 1
    else:
        # If not, LCS is the max of LCS's w/o current char of text1 or text2.
        lcs1 = _lcs_recur(s1, s2, n1 - 1, n2)
        lcs2 = _lcs_recur(s1, s2, n1, n2 - 1)
        result = max(lcs1, lcs2)
    
    return result


def longest_common_subsequence_recur(s1, s2):
    """Longest common subsequence by recursion.

    Time complexity: O(2^n).
    Space complexity: O(n1*n2).
    """
    n1, n2 = len(s1), len(s2)
    return _lcs_recur(s1, s2, n1, n2)


def _lcs_memo(s1, s2, n1, n2, T):
    # Helper function for longest_common_subsequence_memo().
    if n1 == 0 or n2 == 0:
        return 0
    
    if T[n1][n2]:
        return T[n1][n2]

    if s1[n1 - 1] == s2[n2 - 1]:
        # If the current chars are the same, LCS is the last LCS plus 1.
        result = _lcs_memo(s1, s2, n1 - 1, n2 - 1, T) + 1
    else:
        # If not, LCS is the max of LCS's w/o current char of text1 or text2.
        lcs1 = _lcs_memo(s1, s2, n1 - 1, n2 - 1, T)
        lcs2 = _lcs_memo(s1, s2, n1, n2 - 1, T)
        result = max(lcs1, lcs2)

    T[n1][n2] = result
    return result


def longest_common_subsequence_memo(s1, s2):
    """Longest common subsequence by memoization.

    Time complexity: O(n1*n2).
    Space complexity: O(n1*n2).
    """
    n1, n2 = len(s1), len(s2)
    T = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    return _lcs_memo(s1, s2, n1, n2, T)


def longest_common_subsequence_dp(s1, s2):
    """Longest common subsequence by dynamic programming.

    Time complexity: O(n1*n2).
    Space complexity: O(n1*n2).
    """
    n1, n2 = len(s1), len(s2)

    T = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    for r in range(1, n1 + 1):
        for c in range(1, n2 + 1):
            if s1[r - 1] == s2[c - 1]:
                # If the current chars are the same, LCS is the last LCS plus 1.
                T[r][c] = T[r - 1][c - 1] + 1
            else:
                # If not, LCS is the max of LCS's w/o current char of text1 or text2.
                T[r][c] = max(T[r - 1][c], T[r][c - 1])

    return T[-1][-1]


def main():
    import time

    # LCS (BAD): 3.
    s1 = 'BATD'
    s2 = 'ABACD'

    start_time = time.time()
    print('By recursion: {}'.format(longest_common_subsequence_recur(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By memo: {}'.format(longest_common_subsequence_memo(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(longest_common_subsequence_dp(s1, s2)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
