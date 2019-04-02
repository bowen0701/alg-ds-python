"""Leetcode 409. Longest Palindrome
Easy

Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n), where n is the length of string s.
        Space complexity: O(n).
        """
        if len(s) <= 1:
            return len(s)

        letter_d = {}
        for c in s:
            if c in letter_d:
                letter_d[c] += 1
            else:
                letter_d[c] = 1

        lp_len, rem = 0, 0
        for letter in letter_d:
            div, mod = divmod(letter_d[letter], 2)
            lp_len += div * 2
            if mod == 1:
                rem = 1
        lp_len += rem
        return lp_len


def main():
    s = 'abccccdd'  # Ans: 7, since 'dccaccd'.
    print Solution().longestPalindrome(s)

    s = 'Aa'  # Ans: 1, since 'A'.
    print Solution().longestPalindrome(s)


if __name__ == '__main__':
    main()
