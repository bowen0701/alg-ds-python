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
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time complexity: O(m+n).
        Space complexity: O(1).
        """
        if len(s) != len(t):
            return False

        # Create list to collect char a~z's counts.
        char_counts = [0] * 26

        for i in range(len(s)):
            char_counts[ord(s[i]) - ord('a')] += 1
            char_counts[ord(t[i]) - ord('a')] -= 1

        for i in range(26):
            if char_counts[i] != 0:
                return False

        return True


def main():
    # Output: True
    s = "anagram"
    t = "nagaram"
    print(SolutionCharCount().isAnagram(s, t))

    # Output: False
    s = "rat"
    t = "car"
    print(SolutionCharCount().isAnagram(s, t))


if __name__ == '__main__':
    main()
