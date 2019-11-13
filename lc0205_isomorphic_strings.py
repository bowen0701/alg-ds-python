"""Leetcode 205. Isomorphic Strings
Easy

URL: https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""

class SolutionCharMaps(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        Time complexity: O(n), where n is the length of t.
        Space complexity: O(n).
        """
        from collections import defaultdict

        # If both are empty string, return true.
        if not s and not t:
            return True

        # Collect t->s and s->t.
        t_s_char_map = defaultdict()
        s_t_char_map = defaultdict()

        for i in range(len(t)):
            if t[i] not in t_s_char_map:
                t_s_char_map[t[i]] = s[i]
            else:
                if t_s_char_map[t[i]] != s[i]:
                    return False

            if s[i] not in s_t_char_map:
                s_t_char_map[s[i]] = t[i]
            else:
                if s_t_char_map[s[i]] != t[i]:
                    return False

        return True


def main():
    # Output: true
    s = "egg"
    t = "add"
    print SolutionCharMaps().isIsomorphic(s, t)

    # Output: false
    s = "foo"
    t = "bar"
    print SolutionCharMaps().isIsomorphic(s, t)

    # Output: true
    s = "paper"
    t = "title"
    print SolutionCharMaps().isIsomorphic(s, t)

    # Output: False
    s = "aba"
    t = "baa"
    print SolutionCharMaps().isIsomorphic(s, t)


if __name__ == '__main__':
    main()
