"""Leetcode 680. Valid Palindrome II
Easy

URL: https://leetcode.com/problems/valid-palindrome-ii/

Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.
"""

class SolutionNaive(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Note: Time Limit Exceeded

        Time complexity: O(n^3).
        Space complexity: O(n).
        """
        # Check full string.
        if s == s[::-1]:
            return True

        # Check if delete one character.
        for i in range(len(s)):
            s_partial = s[:i] + s[(i+1):]
            if s_partial == s_partial[::-1]:
                return True

        return False


class SolutionTwoPointers(object):
    def _isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply two pointers method.
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # If there is one mismatch, skip left or right char.
                return (self._isPalindrome(s, l + 1, r) or 
                        self._isPalindrome(s, l, r - 1))

            l += 1
            r -= 1

        return True


def main():
    # Output: True
    s = 'aba'
    print SolutionNaive().validPalindrome(s)
    print SolutionTwoPointers().validPalindrome(s)

    # Output: True
    s = 'abca'
    print SolutionNaive().validPalindrome(s)
    print SolutionTwoPointers().validPalindrome(s)

    # Output: False
    s = 'aacb'
    print SolutionNaive().validPalindrome(s)
    print SolutionTwoPointers().validPalindrome(s)


if __name__ == '__main__':
    main()
