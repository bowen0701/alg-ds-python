"""Leetcode 1143. Longest Common Subsequence
Medium

URL: https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with 
some characters(can be none) deleted without changing the relative order of the 
remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length <= 1000
- 1 <= text2.length <= 1000
- The input strings consist of lowercase English characters only.
"""

from typing import List


class SolutionRecur(object):
    def _lcs_recur(self, text1: str, text2: str, n1: int, n2: int) -> int:
        # Base case.
        if n1 == 0 or n2 == 0:
            return 0

        if text1[n1 - 1] == text2[n2 - 1]:
            return self._lcs_recur(text1, text2, n1 - 1, n2 - 1) + 1
        else:
            lcs1 = self._lcs_recur(text1, text2, n1 - 1, n2)
            lcs2 = self._lcs_recur(text1, text2, n1, n2 - 1)
            return max(lcs1, lcs2)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(3^(n1+n2)), where ni is the length of texti.
        Space complexity: O(n1+n2).
        """
        # Apply top-down recursion. 
        n1, n2 = len(text1), len(text2)
        return self._lcs_recur(text1, text2, n1, n2)


class SolutionMemo(object):
    def _lcs_memo(self, text1: str, text2: str, n1: int, n2: int, T: List[List[int]]) -> int:
        # Base case.
        if n1 == 0 or n2 == 0:
            return 0

        # Check memo table.
        if T[n1][n2]:
            return T[n1][n2]

        if text1[n1 - 1] == text2[n2 - 1]:
            result = self._lcs_memo(text1, text2, n1 - 1, n2 - 1, T) + 1
        else:
            lcs1 = self._lcs_memo(text1, text2, n1 - 1, n2, T)
            lcs2 = self._lcs_memo(text1, text2, n1, n2 - 1, T)
            result = max(lcs1, lcs2)

        T[n1][n2] = result
        return result

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n1*n2), where ni is the length of texti.
        Space complexity: O(n1*n2).
        """
        # Apply top-down recursion with memoization.
        n1, n2 = len(text1), len(text2)
        T = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        return self._lcs_memo(text1, text2, n1, n2, T)


class SolutionDP(object):
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n1*n2), where ni is the length of texti.
        Space complexity: O(n1*n2).
        """
        # Apply bottom-up dynamic programming.
        n1, n2 = len(text1), len(text2)

        # Create memoization table of n1*n2.
        T = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for r in range(1, n1 + 1):
            for c in range(1, n2 + 1):
                # Since char idx is from 0 ~ n_i - 1.
                if text1[r - 1] == text2[c - 1]:
                    # If the current chars are the same, LCS is the last LCS plus 1.
                    T[r][c] = T[r - 1][c - 1] + 1
                else:
                    # If not, LCS is the max of LCS's w/o current char of text1 or text2.
                    T[r][c] = max(T[r - 1][c], T[r][c - 1])

        return T[-1][-1]


def main():
    # Ans: 3.
    text1 = "abcde"
    text2 = "ace" 
    print(SolutionRecur().longestCommonSubsequence(text1, text2))
    print(SolutionMemo().longestCommonSubsequence(text1, text2))
    print(SolutionDP().longestCommonSubsequence(text1, text2))

    # Ans: 3
    text1 = "abc"
    text2 = "abc"
    print(SolutionRecur().longestCommonSubsequence(text1, text2))
    print(SolutionMemo().longestCommonSubsequence(text1, text2))
    print(SolutionDP().longestCommonSubsequence(text1, text2))

    # Ans: 0
    text1 = "abc"
    text2 = "def"   
    print(SolutionRecur().longestCommonSubsequence(text1, text2))
    print(SolutionMemo().longestCommonSubsequence(text1, text2))
    print(SolutionDP().longestCommonSubsequence(text1, text2))


if __name__ == '__main__':
    main()
