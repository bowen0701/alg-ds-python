"""Leetcode 151. Reverse Words in a String
Medium

Given an input string, reverse the string word by word. 

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single 
space in the reversed string.
 

Note:
A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed 
string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the 
reversed string.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        pass


def main():
    import time

    # Ans: "blue is sky the".
    s = 'the sky is blue'

    # Ans: "world! hello".
    s = '  hello world!  '

    # Ans: "example good a".
    s = 'a good   example'


if __name__ == '__main__':
    main()
