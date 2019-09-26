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

class SolutionDict(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n), where n is the length of string s.
        Space complexity: O(n).
        """
        if len(s) <= 1:
            return len(s)

        # Get letter->count dictionary.
        letter_d = {}
        for l in s:
            if l in letter_d:
                letter_d[l] += 1
            else:
                letter_d[l] = 1

        # Compute how many letters occur in even times.
        lp_len, rem = 0, 0
        for letter in letter_d:
            div, mod = divmod(letter_d[letter], 2)
            lp_len += div * 2

            # If there is any letter remaining modulus is 1,
            # set remainder to 1, which is a valid palindrome char.
            if mod == 1:
                rem = 1

        lp_len += rem
        return lp_len


def main():
    s = 'abccccdd'  # Ans: 7, since 'dccaccd'.
    print SolutionDict().longestPalindrome(s)

    s = 'Aa'  # Ans: 1, since 'A'.
    print SolutionDict().longestPalindrome(s)


if __name__ == '__main__':
    main()
