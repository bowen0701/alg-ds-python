"""Leetcode 5. Longest Palindromic Substring
Medium

URL: https://leetcode.com/problems/longest-palindromic-substring/

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

class SolutionBrute(object):
    def longestPalindrome(self, s: str) -> str:
        """
        Time complexity: O(n^3).
        Space complexity: O(n).
        """
        lps = ''

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1] and j - i > len(lps):
                    lps = s[i:j]

        return lps


class SolutionDP(object):
    def longestPalindrome(self, s: str) -> str:
        """
        Apply dynamic programming with botton-up memoization,
        but track longest palindrom.

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        if not s:
            return ''

        n = len(s)
        T = [[False] * n for _ in range(n)]

        # Set each char as palindrom.
        for i in range(n):
            T[i][i] = True
            start = i
            max_len = 1
            
        # Check if consecutive char pair is palindrom.
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                T[i][i + 1] = True
                start = i
                max_len = 2

        # Use two pointer method with start i & end j in gaps >= 2 to
        # check they are equal and substring from i+1 to j-1 is palindrome. 
        for j in range(2, n):
            for i in range(j - 1):
                if s[i] == s[j] and T[i + 1][j - 1]:
                    T[i][j] = True
                    if j - i + 1 > max_len:
                        start = i
                        max_len = j - i + 1

        return s[start:(start + max_len)]


class SolutionIter(object):
    def longestPalindrome(self, s: str) -> str:
        """
        Apply iteration.

        Time complexity: O(n^2).
        Space complexity: O(n).
        """
        if not s:
            return ''

        start = 0
        max_len = 1

        # If we increase s by 1 character, we could only increase LPS by 2 or 1.
        for j in range(1, len(s)):
            # Increase LPS by 2: check start's left and end's right.
            if (j - max_len >= 1 and 
                s[(j - max_len - 1):(j + 1)] == s[(j - max_len - 1):(j + 1)][::-1]):
                start = j - max_len - 1
                max_len += 2
                continue

            # Increase LPS by 1: check end's right only.
            if (j - max_len >= 0 and 
                s[(j - max_len):(j + 1)] == s[(j - max_len):(j + 1)][::-1]):
                start = j - max_len
                max_len += 1

        return s[start:(start + max_len)]


def main():
    import time

    s = 'babad'    # Ans: bab.
   
    start_time = time.time()
    print('By brute force: {}'.format(SolutionBrute().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter: {}'.format(SolutionIter().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    s = 'cbbd'     # Ans: bb.

    start_time = time.time()
    print('By brute force: {}'.format(SolutionBrute().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter: {}'.format(SolutionIter().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    s = 'abcba'    # Ans: abcba

    start_time = time.time()
    print('By brute force: {}'.format(SolutionBrute().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By DP: {}'.format(SolutionDP().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By iter: {}'.format(SolutionIter().longestPalindrome(s)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
