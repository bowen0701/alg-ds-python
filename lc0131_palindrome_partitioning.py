"""Leetcode 131. Palindrome Partitioning
Medium

URL: https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that 
every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class SolutionBacktrack(object):
    def _backtrack(self, result, tmps, s, start):
        if start == len(s):
            # Check partial string with start len(s): empty string ''.
            # Palindrom partition is completed.
            result.append(tmps[:])
            return None

        for i in range(start, len(s)):
            # Check partial string s[start:i+1] is palindrome.
            partial = s[start:i+1]
            if partial == partial[::-1]:
                # If yes, append it to tmps.
                tmps.append(partial)

                # Further check the remaining string is also a palinfrome.
                self._backtrack(result, tmps, s, i + 1)

                # Backtrack by popping out the top tmps.
                tmps.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]

        Time complexity: O(n*2^n), where n is the length of s.
        Space complexity: O(n).
        """
        # Apply backtracking.
        result = []
        tmps = []

        start = 0
        self._backtrack(result, tmps, s, start)

        return result


def main():
    s = "aab"
    print SolutionBacktrack().partition(s)


if __name__ == '__main__':
    main()
