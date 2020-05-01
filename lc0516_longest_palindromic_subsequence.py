"""Leetcode 516. Longest Palindromic Subsequence
Medium

URL: https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

class SolutionRecur(object):
    def _LPS(self, s, l, r):
        if l > r:
            return 0

        if l == r:
            return 1

        if s[l] == s[r]:
            # Check LPS in subsequence between s[l] and s[r].
            return self._LPS(s, l + 1, r - 1) + 2
        else:
            # Check max of LPS's in s[l+1:r-1] and s[l:r].
            return max(self._LPS(s, l + 1, r), self._LPS(s, l, r - 1))

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        Note: Time Limit Exceeded.

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Apply top-down DP by recursion.
        l, r = 0, len(s) - 1
        return self._LPS(s, l, r)


class SolutionMemo(object):
    def _LPS(self, s, l, r, T):
        if l > r:
            return 0

        if T[l][r]:
            return T[l][r]

        if l == r:
            T[l][l] = 1

        if s[l] == s[r]:
            # Check LPS in subsequence between s[l] and s[r].
            T[l][r] = self._LPS(s, l + 1, r - 1, T) + 2
        else:
            # Check max of LPS's in s[l+1:r-1] and s[l:r].
            T[l][r] = max(self._LPS(s, l + 1, r, T), self._LPS(s, l, r - 1, T))

        return T[l][r]

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        # Apply top-down DP by recursion with memoization.
        n = len(s)
        T = [[None] * n for _ in range(n)]

        l, r = 0, len(s) - 1
        return self._LPS(s, l, r, T)


class SolutionDP(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        # Apply bottom-up dynamic programming.
        n = len(s)
        T = [[0] * n for _ in range(n)]

        # Starting from tail with bottom-up.
        for l in range(n - 1, -1, -1):
            T[l][l] = 1

            for r in range(l + 1, n):
                if s[l] == s[r]:
                    T[l][r] = T[l + 1][r - 1] + 2
                else:
                    T[l][r] = max(T[l][r - 1], T[l + 1][r])

        return T[0][-1]


def main():
    # Output: 4.
    s = "bbbab"
    print SolutionRecur().longestPalindromeSubseq(s)
    print SolutionMemo().longestPalindromeSubseq(s)
    print SolutionDP().longestPalindromeSubseq(s)

    # Output: 2.
    s = "cbbd"
    print SolutionRecur().longestPalindromeSubseq(s)
    print SolutionMemo().longestPalindromeSubseq(s)
    print SolutionDP().longestPalindromeSubseq(s)


if __name__ == '__main__':
    main()
