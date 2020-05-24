"""Leetcode 10. Regular Expression matching
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

class SolutionDP(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        Regular expression matching by bottom-up dynamic programming.

        Time complexity: O(m*n), where m is the length of string, and
          n is the lenght of pattern.
        Space complexity: O(m*n).
        """
        # Edge cases.
        if not s and not p:
            return True
        if not s or not p:
            return False

        # Apply Dynamic Programming with s x p tabular. 
        T = [[False] * (len(p) + 1) for _ in range((len(s) + 1))]

        # For empty s matches empty p.
        T[0][0] = True

        # For T[i][0] = False, as s does not match empty p = ''.
        # For T[0][j] = True as empty s matches p = a*b*c*, with '*' at even pos.
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                T[0][j] = T[0][j - 2]

        # Update the table for s's char along the p's char.
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    # Match without s[i] & p[j].
                    T[i][j] = T[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if s[i - 1] != p[j - 2] and p[j - 2] != '.':
                        # Match without a*.
                        T[i][j] = T[i][j - 2]
                    else:
                        # Since s[i-1] = p[j-2] or p[j-2] = '.',
                        # match with a or without a* or ignoring s[i].
                        T[i][j] = T[i][j - 1] or T[i][j - 2] or T[i - 1][j]


        return T[-1][-1]


def main():
    s = "aa"
    p = "a"
    # Output: false.
    print SolutionDP().isMatch(s, p)

    s = "aa"
    p = "a*"
    # Output: true.
    print SolutionDP().isMatch(s, p)

    s = "ab"
    p = ".*"
    # Output: true.
    print SolutionDP().isMatch(s, p)

    s = "aab"
    p = "c*a*b"
    # Output: true.
    print SolutionDP().isMatch(s, p)

    s = "mississippi"
    p = "mis*is*p*."
    # Output: false.
    print SolutionDP().isMatch(s, p)


if __name__ == '__main__':
    main()
