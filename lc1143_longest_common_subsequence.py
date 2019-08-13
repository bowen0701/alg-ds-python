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


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int

        Time complexity: O(n1*n2), where ni is the length of texti.
        Space complexity: O(n1*n2).
        """
        # By bottom-up dynamic programming.
        n1, n2 = len(text1), len(text2)

        # Create memoization table.
        M = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for r in range(1, n1 + 1):
            for c in range(1, n2 + 1):
                # Since char idx is from 0 ~ n_i - 1.
                if text1[r - 1] == text2[c - 1]:
                    # If the current chars are the same, LCS is the last LCS plus 1.
                    M[r][c] = M[r - 1][c - 1] + 1
                else:
                    # If not, LCS is the max of LCS's w/o current char of text1 or text2.
                    M[r][c] = max(M[r - 1][c], M[r][c - 1])

        return M[-1][-1]


def main():
    # Ans: 3.
    text1 = "abcde"
    text2 = "ace" 
    print Solution().longestCommonSubsequence(text1, text2)

    # Ans: 3
    text1 = "abc"
    text2 = "abc"
    print Solution().longestCommonSubsequence(text1, text2)

    # Ans: 0
    text1 = "abc"
    text2 = "def"
    print Solution().longestCommonSubsequence(text1, text2)


if __name__ == '__main__':
    main()
