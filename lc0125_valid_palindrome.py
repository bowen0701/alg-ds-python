"""Leetcode 125. Valid Palindrome
Easy

URL: https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""

class SolutionReverse(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Take lower, convert to list, and keep alphanumetic chars.
        s_converted = [c for c in list(s.lower()) if 
                       0 <= ord(c) - ord('a') <= 25 or
                       0 <= ord(c) - ord('0') <= 9]

        # Compare list with its reverse.
        return s_converted == s_converted[::-1]


class SolutionTwoPointers(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply two pointers from the leftmost and rightmost.
        i, j = 0, len(s) - 1

        while i < j:
            # Skip if not alphanumeric chars.
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


def main():
    # Ans: True
    s = "A man, a plan, a canal: Panama"
    print SolutionReverse().isPalindrome(s)
    print SolutionTwoPointers().isPalindrome(s)

    # Ans: False
    s = "0P"
    print SolutionReverse().isPalindrome(s)
    print SolutionTwoPointers().isPalindrome(s)


if __name__ == '__main__':
    main()
