"""Leetcode 647. Palindromic Substrings
Medium

URL: https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different
substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

class SolutionCenterExpandTwoPointers(object):
    def _extendPalindrome(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.n_pals += 1

            # Expand to two sides to check bigger palindrome.
            left -= 1
            right += 1

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int

        Expand palindrome from center with two pointers.

        Time complexity: O(n^2).
        Space complexity: O(1).
        """
        self.n_pals = 0

        for i in range(len(s)):
            # Extend palindrome with odd length.
            self._extendPalindrome(i, i, s)

            # Extend palindrome with even length.
            self._extendPalindrome(i, i + 1, s)

        return self.n_pals


def main():
    # Output: 3.
    s = "abc"
    print SolutionCenterExpandTwoPointers().countSubstrings(s)

    # Output: 6.
    s = "aaa"
    print SolutionCenterExpandTwoPointers().countSubstrings(s)


if __name__ == '__main__':
    main()
