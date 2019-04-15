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

        Time limit exceeded.
        """
        n = len(s)
        max_len = 1
        max_i = 0
        max_j = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if s[i:(j + 1)] == s[i:(j + 1)][::-1]:
                    ij_len = j - i + 1
                    if ij_len > max_len:
                        max_len = ij_len
                        max_i = i
                        max_j = j
        return s[max_i:(max_j + 1)]


class SolutionDP(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not len(s):
            return ''

        n = len(s)
        M = [[False] * n for _ in range(n)]

        for i in range(n):
            M[i][i] = True
            max_len = 1
            s_pal = s[i]
            
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                M[i][i + 1] = True
                max_len = 2
                s_pal = s[i:(i + 2)]

        for j in range(n):
            for i in range(0, j - 1):
                if s[i] == s[j] and M[i + 1][j - 1]:
                    M[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        s_pal = s[i:(j + 1)]
        return s_pal


def main():
    import time

    s = 'babad'    # Ans: bab.
    
    start_time = time.time()
    print('By naive: {}'
          .format(SolutionNaive().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))


    s = 'cbbd'     # Ans: bb.

    start_time = time.time()
    print('By naive: {}'
          .format(SolutionNaive().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    s = 'abcba'    # Ans: abcba

    start_time = time.time()
    print('By naive: {}'
          .format(SolutionNaive().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
