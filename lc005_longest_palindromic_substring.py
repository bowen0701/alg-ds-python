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

        Apply dynamic programming with botton-up memoization,
        but track longest palindrom.

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        if not len(s):
            return ''

        n = len(s)
        T = [[False] * n for _ in range(n)]

        for i in range(n):
            T[i][i] = True
            start = i
            max_len = 1
            
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                T[i][i + 1] = True
                start = i
                max_len = 2

        for j in range(2, n):
            for i in range(0, j):
                if s[i] == s[j] and T[i + 1][j - 1]:
                    T[i][j] = True
                    if j - i + 1 > max_len:
                        start = i
                        max_len = j - i + 1

        return s[start:(start + max_len)]


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
