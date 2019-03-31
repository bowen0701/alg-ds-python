from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def longest_common_subsequence_recur(s1, s2, n1, n2):
    """Longest common subsequence by recursion.

    Time complexity: O(2^n).
    Space complexity: O(n1*n2).
    """
    if n1 < 0 or n2 < 0:  # Base case.
        lcs = 0
    elif s1[n1] == s2[n2]:
        lcs = 1 + longest_common_subsequence_recur(
            s1, s2, n1 - 1, n2 - 1)
    elif s1[n1] != s2[n2]:  # Just for clarity.
        lcs1 = longest_common_subsequence_recur(s1, s2, n1 - 1, n2)
        lcs2 = longest_common_subsequence_recur(s1, s2, n1, n2 - 1)
        lcs = max(lcs1, lcs2)
    return lcs


def _lcs_memo(s1, s2, n1, n2, M):
    if M[n1][n2]:
        return M[n1][n2]

    if n1 < 0 or n2 < 0:
        lcs = 0
    elif s1[n1] == s2[n2]:
        lcs = 1 + _lcs_memo(s1, s2, n1 - 1, n2 - 1, M)
    elif s1[n1] != s2[n2]:
        lcs1 = _lcs_memo(s1, s2, n1 - 1, n2 - 1, M)
        lcs2 = _lcs_memo(s1, s2, n1, n2 - 1, M)
        lcs = max(lcs1, lcs2)
    M[n1][n2] = lcs
    return lcs


def longest_common_subsequence_memo(s1, s2, n1, n2):
    """Longest common subsequence by memoization.

    Time complexity: O(n1*n2).
    Space complexity: O(n1*n2).
    """
    M = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    return _lcs_memo(s1, s2, n1, n2, M)


def longest_common_subsequence_dp(s1, s2, n1, n2):
    """Longest common subsequence by dynamic programming.

    Time complexity: O(n1*n2).
    Space complexity: O(n1*n2).
    """ 
    M = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    for r in range(1, n1 + 1):
        for c in range(1, n2 + 1):
            if s1[r] == s2[c]:
                M[r][c] = 1 + M[r - 1][c - 1]
            elif s1[r] != s2[c]:
                lcs1 = M[r - 1][c]
                lcs2 = M[r][c - 1]
                M[r][c] = max(lcs1, lcs2)
    return M[-1][-1]


def main():
    import time

    s1 = 'BATD'
    s2 = 'ABACD'  # LCD: 3 (BAD).
    n1 = len(s1) - 1
    n2 = len(s2) - 1

    start_time = time.time()
    print('LCD by recursion: {}'.format(
        longest_common_subsequence_recur(s1, s2, n1, n2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('LCD by memo: {}'.format(
        longest_common_subsequence_memo(s1, s2, n1, n2)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('LCD by DP: {}'.format(
        longest_common_subsequence_memo(s1, s2, n1, n2)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
