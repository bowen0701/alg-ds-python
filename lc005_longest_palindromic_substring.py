"""Leetcode 5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

class SolutionNaive(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        Time complexity: O(n^3).
        Space complexity: O(1).
        """
        pal_s = ''

        for i in range(len(s)):
            for j in range(1, len(s) + 1):
                if s[i:j] == s[i:j][::-1] and j - i > len(pal_s):
                    pal_s = s[i:j]

        return pal_s


class SolutionDP(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        Time complexity: O(n^3).
        Space complexity: O(n^2).
        """
        if not len(s):
            return ''

        n = len(s) - 1
        M = [[False] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            M[i][i] = True
            max_len = 1
            pal_s = s[i]
            
        for i in range(n):
            if s[i] == s[i + 1]:
                M[i][i + 1] = True
                max_len = 2
                pal_s = s[i:(i + 2)]

        for j in range(n + 1):
            for i in range(0, j - 1):
                if s[i] == s[j] and M[i + 1][j - 1]:
                    M[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        pal_s = s[i:(j + 1)]
        return pal_s


def main():
    import time

    s = 'babad'    # Ans: bab.
   
    start_time = time.time()
    print('By naive: {}'.format(SolutionNaive().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    s = 'cbbd'     # Ans: bb.

    start_time = time.time()
    print('By naive: {}'.format(SolutionNaive().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    s = 'abcba'    # Ans: abcba

    start_time = time.time()
    print('By naive: {}'.format(SolutionNaive().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
