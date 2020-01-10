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

class SolutionDictDoubleEvenOneOdd(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n), where n is the length of string s.
        Space complexity: O(n).
        """
        from collections import defaultdict

        if len(s) <= 1:
            return len(s)

        # Create dict: letter->count.
        letter_count_d = defaultdict(int)
        for l in s:
            letter_count_d[l] += 1

        # Compute how many letters occur in even times.
        pal_len, odd = 0, 0

        for l in letter_count_d:
            div, mod = divmod(letter_count_d[l], 2)
            pal_len += div * 2

            # If there is any letter number is odd, add one valid letter.
            if mod == 1:
                odd = 1

        pal_len += odd
        return pal_len


def main():
    s = 'abccccdd'  # Ans: 7, since 'dccaccd'.
    print SolutionDictDoubleEvenOneOdd().longestPalindrome(s)

    s = 'Aa'  # Ans: 1, since 'A'.
    print SolutionDictDoubleEvenOneOdd().longestPalindrome(s)


if __name__ == '__main__':
    main()
