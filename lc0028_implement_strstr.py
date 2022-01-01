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


class SolutionBruteForce:
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
    def _kmp_preprocess(self, needle: str) -> List[int]:
        n_needle = len(needle)

        # Preprosss needle to get lps which indicates longest proper prefix which is also suffix:
        # Specifically, for each sub-pattern needle[0:i], where i = 0 to m-1, 
        # lps[i] stores length of the maximum matching proper prefix which is also a suffix.
        lps = [0] * n_needle

        length = 0
        j = 1

        while j < n_needle:
            if needle[j] == needle[length]:
                length += 1
                lps[j] = length
                j += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[j] = 0
                j += 1

        return lps

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Time complexity: O(n + m)
          - n is the length of haystack,
          - m is the length of needle.
        Space complexity: O(m).
        """
        # Apply KMP (Knuth, Morris & Pratt) pattern searching algorithm.

        # Edge case.
        if not needle:
            return 0

        n_haystack, n_needle = len(haystack), len(needle)

        # Get KMP longest prefix suffix.
        lps = self._kmp_preprocess(needle)

        # Use a value from lps[] to decide the next characters to be matched:
        # Specifically, When we see a mismatch, we know that characters needle[0:j-1] match with haystack[i-j:i-1].
        # We also know lps[j-1] is count of characters of needle[0:j-1] that are both proper prefix and suffix.
        i = j = 0
        while i < n_haystack:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            if j == n_needle:
                return i - j
            elif i < n_haystack and haystack[i] != needle[j]:
                # Mismatch after j matches.
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1


def main():
    import time

    # Output: 2
    haystack = "hello"
    needle = "ll"

    start_time = time.time()
    print(SolutionBruteForce().strStr(haystack, needle))
    print(f"Time for brute force: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionKMP().strStr(haystack, needle))
    print(f"Time for KMP: {time.time() - start_time}")

    # Output: -1
    haystack = "aaaaa"
    needle = "bba"

    start_time = time.time()
    print(SolutionBruteForce().strStr(haystack, needle))
    print(f"Time for brute force: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionKMP().strStr(haystack, needle))
    print(f"Time for KMP: {time.time() - start_time}")



if __name__ == '__main__':
    main()
