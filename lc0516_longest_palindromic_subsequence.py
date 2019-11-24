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
    def _LPS(self, s, left, right):
        if left > right:
            return 0

        if left == right:
            return 1

        if s[left] == s[right]:
            # Then check LPS in s[left+1:right].
            return self._LPS(s, left + 1, right - 1) + 2
        else:
            # Then check max of LPS's in s[left+1:right-1] and s[left:right].
            return max(self._LPS(s, left + 1, right), 
                       self._LPS(s, left, right - 1))

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        Note: Time Limit Exceeded.

        Time complexity: O(2^n).
        Space complexity: O(n).
        """
        # Apply top-down recursion.
        left, right = 0, len(s) - 1
        return self._LPS(s, left, right)


class SolutionMemo(object):
    def _LPS(self, s, left, right, T):
        if T[left][right]:
            return T[left][right]

        if left > right:
            return 0

        if s[left] == s[right]:
            # Then check LPS in s[left+1:right].
            T[left][right] = self._LPS(s, left + 1, right - 1, T) + 2
        else:
            # Then check max of LPS's in s[left+1:right-1] and s[left:right].
            T[left][right] = max(self._LPS(s, left + 1, right, T), 
                                 self._LPS(s, left, right - 1, T))
        return T[left][right]

    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        # Apply top-down recursion with memoization.
        n = len(s)
        T = [[None] * n for _ in range(n)]

        for i in range(n):
            T[i][i] = 1

        left, right = 0, len(s) - 1
        return self._LPS(s, left, right, T)


def main():
    # Output: 4.
    s = "bbbab"
    print SolutionRecur().longestPalindromeSubseq(s)
    print SolutionMemo().longestPalindromeSubseq(s)

    # Output: 2.
    s = "cbbd"
    print SolutionRecur().longestPalindromeSubseq(s)
    print SolutionMemo().longestPalindromeSubseq(s)


if __name__ == '__main__':
    main()
