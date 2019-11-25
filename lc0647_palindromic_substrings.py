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

class SolutionCenterExpansion(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n^2).
        Space complexity: O(1).
        """
        n = len(s)
        n_palindromes = 0

        # Iterate to check palindrome starting from 2*n-1 center expansions.
        for i in range(2 * n - 1):
            left = i // 2
            right = (i + 1) // 2
            while left >=0 and right < n and s[left] == s[right]:
                # If palindrome, expand to left/right char to further check.
                n_palindromes += 1
                left -= 1
                right += 1

        return n_palindromes


def main():
    # Output: 3.
    s = "abc"
    print SolutionCenterExpansion().countSubstrings(s)

    # Output: 6.
    s = "aaa"
    print SolutionCenterExpansion().countSubstrings(s)


if __name__ == '__main__':
    main()
