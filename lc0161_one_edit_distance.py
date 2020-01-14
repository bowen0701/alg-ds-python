"""Leetcode 161. One Edit Distance (Premium)
Medium

URL: https://leetcode.com/problems/one-edit-distance

Given two strings s and t, determine if they are both one edit distance apart.

Note:
There are 3 possiblities to satisify one edit distance apart:
- Insert a character into s to get t
- Delete a character from s to get t
- Replace a character of s to get t

Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Example 2:
Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.

Example 3:
Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""

class SolutionOneLengthDiff(object):
    def _one_replace(self, s, t):
        # Iterate through s, check how many chars are different.
        n_replaced = 0

        for i in range(len(s)):
            if s[i] != t[i]:
                n_replaced += 1

        return n_replaced == 1

    def _one_insert(self, s, t):
        # Iterate through two pointers, check how many chars are inserted.
        n_replaced = 0

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                n_replaced += 1
                if n_replaced > 1:
                    return False
                j += 1
            else:
                i += 1
                j += 1

        return True

    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Check if length difference is larger than 1.
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) == len(t):
            # If s is of equal lenght with t, replace a char from s and t.
            return self._one_replace(s, t)
        elif len(s) == len(t) - 1:
            # If s is shorter than t by one char, insert a char into s.
            return self._one_insert(s, t)
        elif len(s) == len(t) + 1:
            # If s is longer than t by one char, delete a char from s,
            # which is equivalent to insert a char into t.
            return self._one_insert(t, s)


def main():
    # Output: true (by insert)
    s = "ab"
    t = "acb"
    print SolutionOneLengthDiff().isOneEditDistance(s, t)

    # Output: false
    s = "cab" 
    t = "ad"
    print SolutionOneLengthDiff().isOneEditDistance(s, t)

    # Output: true (by replace)
    s = "1203"
    t = "1213"
    print SolutionOneLengthDiff().isOneEditDistance(s, t)

    # Output: false
    s = ""
    t = ""
    print SolutionOneLenghtDiff().isOneEditDistance(s, t)


if __name__ == '__main__':
    main()
