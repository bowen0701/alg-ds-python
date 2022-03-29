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

class SolutionCenterExpandTwoPointers:
    def _expandPalindrome(self, left: int, right: int, s: str) -> None:
        while left >= 0 and right < len(s):
            # Stop expanding to two sides.
            if s[left] != s[right]:
                break

            # Expand to two sides to check bigger palindrome.
            self.result += 1
            left -= 1
            right += 1

    def countSubstrings(self, s: str) -> int: 
        """
        Expand palindrome from center with two pointers.

        Time complexity: O(n^2).
        Space complexity: O(1).
        """
        self.result = 0

        for i in range(len(s)):
            # Expand palindrome of odd and even length.
            self._expandPalindrome(i, i, s)
            self._expandPalindrome(i, i + 1, s)

        return self.result


def main():
    # Output: 3.
    s = "abc"
    print(SolutionCenterExpandTwoPointers().countSubstrings(s))

    # Output: 6.
    s = "aaa"
    print(SolutionCenterExpandTwoPointers().countSubstrings(s))


if __name__ == '__main__':
    main()
