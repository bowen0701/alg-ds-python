"""Leetcode 242. Valid Anagram
Easy

URL: https://leetcode.com/problems/valid-anagram/

Given two strings s and t,
write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class SolutionCharCount(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # Create lists to collect char a~z's counts.
        s_char_counts = [0] * 26
        t_char_counts = [0] * 26

        for c in s:
            idx = ord(c) - ord('a')
            s_char_counts[idx] += 1

        for c in t:
            idx = ord(c) - ord('a')
            t_char_counts[idx] += 1

        for i in range(26):
            if s_char_counts[i] != t_char_counts[i]:
                return False

        return True


def main():
    # Output: True
    s = "anagram"
    t = "nagaram"
    print SolutionCharCount().isAnagram(s, t)

    # Output: False
    s = "rat"
    t = "car"
    print SolutionCharCount().isAnagram(s, t)


if __name__ == '__main__':
    main()
