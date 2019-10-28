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
    def _backtrack(self, result, temp, s, start):
        if start == len(s):
            # Use shallow copy.
            result.append(temp[:])
            return None

        # Iterate starting from start.
        for i in range(start, len(s)):
            # Check partial string s[start:i+1] is palindrome.
            partial = s[start:i+1]
            if partial == partial[::-1]:
                temp.append(partial)

                # Further check the remaining string is also a palinfrome.
                self._backtrack(result, temp, s, i + 1)

                # Pop for backtracking.
                temp.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]

        Time complexity: O(n*2^n), where n is the length of s.
        Space complexity: O(n).
        """
        # Apply backtracking.
        result = []
        temp = []
        start = 0
        self._backtrack(result, temp, s, start)
        return result


def main():
    s = "aab"
    print SolutionBacktrack().partition(s)


if __name__ == '__main__':
    main()
