"""Leetcode 266. Palindrome Permutation (Premium)
Easy

URL: https://leetcode.com/problems/palindrome-permutation

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true
"""

class SolutionOneOddCharCounts(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import defaultdict

        if not s:
            return True

        # Count char counts; palindrome permutation only has one odd char count.
        char_counts = defaultdict(int)
        for c in s:
            char_counts[c] += 1

        n_odd_chars = 0
        for k, v in char_counts.items():
            if v % 2 == 1:
                n_odd_chars += 1

            if n_odd_chars >= 2:
                return False

        return True


def main():
    # Output: false
    s = "code"
    print SolutionOneOddCharCounts().canPermutePalindrome(s)

    # Output: true
    s = "aab"
    print SolutionOneOddCharCounts().canPermutePalindrome(s)

    # Output: true
    s = "carerac"
    print SolutionOneOddCharCounts().canPermutePalindrome(s)


if __name__ == '__main__':
    main()
