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

        len_haystack, len_needle = len(haystack), len(needle)

        # Iteratively starting from the left, match sliding windows.
        for i in range(len_haystack - len_needle + 1):
            if haystack[i:(i+len_needle)] == needle:
                return i

        return -1


class SolutionKmp:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity
        Space complexity
        """
        pass


def main():
    haystack = "hello"
    needle = "ll"
    print SolutionSlidingWindowMatch().strStr(haystack, needle)

    haystack = "aaaaa"
    needle = "bba"
    print SolutionSlidingWindowMatch().strStr(haystack, needle)


if __name__ == '__main__':
    main()
