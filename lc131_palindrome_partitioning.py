"""Leetcode 131. Palindrome Partitioning
Medium

URL: https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def _backtrack(self, result, temps, s, start):
        if start == len(s):
            result.append(temps[:])
            return None

        for i in range(start, len(s)):
            # Check if palindrome.
            if s[start:i+1] == s[start:i+1][::-1]:
                temps.append(s[start:i+1])
                self._backtrack(result, temps, s, i + 1)
                temps.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # Apply backtracking.
        result = []
        temps = []
        start = 0
        self._backtrack(result, temps, s, start)
        return result


def main():
    s = "aab"
    print Solution().partition(s)


if __name__ == '__main__':
    main()
