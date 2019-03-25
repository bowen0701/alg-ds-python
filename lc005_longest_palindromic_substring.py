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
                else:
                    break
        return s[max_i:(max_j + 1)]


class SolutionDP(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pass


def main():
    s = 'babad'    # Ans: bab.
    print(SolutionNaive().longestPalindrome(s))

    s = 'cbbd'     # Ans: bb.
    print(SolutionNaive().longestPalindrome(s))


if __name__ == '__main__':
    main()
