"""Leetcode 58. Length of Last Word
Easy

URL: https://leetcode.com/problems/length-of-last-word/

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

Example:
Input: "Hello World"
Output: 5
"""

class SolutionSplit(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not s:
            return 0

        # Strip and then split s with separator ' '.
        splitted_s = s.strip().split(' ')

        # Return last word's length.
        return len(splitted_s[-1])


def main():
    # Output: 5
    s = "Hello World"
    print SolutionSplit().lengthOfLastWord(s)


if __name__ == '__main__':
    main()
