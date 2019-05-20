"""Leetcode 10. Regular Expression Matching
Hard

URL: https://leetcode.com/problems/regular-expression-matching/

Given an input string (s) and a pattern (p), implement regular expression 
matching with support for '.' and '*'.
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Note:
- s could be empty and contains only lowercase letters a-z.
- p could be empty and contains only lowercase letters a-z, and 
  characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. 
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. 
Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        Regular expression matching by bottom-up dynamic programming.

        Time complexity: O(m*n).
        Space complexity: O(m*n).
        """
        T = [[False] * (len(p) + 1) for _ in range((len(s) + 1))]

        # For empty s and p.
        T[0][0] = True

        # For empty s and p = a*, a*b*, or a*b*c*.
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                T[0][j] = T[0][j - 2]

        # Update the table for s's char along the p's char.
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i] == p[j] or p[j] == '.':
                    # Check match without s[i] & p[j].
                    T[i][j] = T[i - 1][j - 1]
                elif p[j] == '*':
                    # Check match for p before a*.
                    T[i][j] = T[i][j - 2]
                    if s[i] == p[j - 1] or p[j - 1] == '.':
                        # Further check s[i] and char or '.' before '*'.
                        T[i][j] |= T[i - 1][j]

        return T[-1][-1]


def main():
    s = "aa"
    p = "a"
    # Output: False.
    print Solution().isMatch(s, p)


if __name__ == '__main__':
    main()
