"""Leetcode 28. Implement strStr()
Easy

URL: https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? 
This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().
"""

from typing import List


class SolutionSlidingWindowMatch:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n*m), where 
          - n is the length of haystack,
          - m is the length of needle.
        Space complexity: O(m).
        """
        # Edge cases.
        if not needle:
            return 0

        if not haystack:
            return -1

        n_haystack, n_needle = len(haystack), len(needle)

        # Iteratively starting from the left, match sliding windows.
        for i in range(n_haystack - n_needle + 1):
            if haystack[i:(i+n_needle)] == needle:
                return i

        return -1


class SolutionKMP:
    def _kmp_longest_prefix_suffix(self, needle: str) -> List[int]:
        n_needle = len(needle)
        T = [0]

    def _kmp_substring_search(self, haystack: str, needle: str) -> bool:
        # Edge case.
        if not needle:
            return False

        n_haystack, n_needle = len(haystack), len(needle)

        # TODO: continue implementation for KMP substring search.
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity
        Space complexity
        """
        result = self._kmp_substring_search(haystack, needle)
        if result < len(haystack):
            return result
        else:
            return -1


def main():
    # Output: 2
    haystack = "hello"
    needle = "ll"
    print(SolutionSlidingWindowMatch().strStr(haystack, needle))

    # Output: -1
    haystack = "aaaaa"
    needle = "bba"
    print(SolutionSlidingWindowMatch().strStr(haystack, needle))


if __name__ == '__main__':
    main()
