"""Leetcode 394. Decode String
Medium

URL: https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the 
square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and 
that digits are only for those repeat numbers, k. 
For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str

        Time complexity: O(m*n), where 
          - m is the length of string, and
          - n is maximun number.
        Space complexity: O(m).
        """
        stack = [['', 1]]
        num = ''

        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(['', int(num)])
                num = ''
            elif c == ']':
                # Concat the characters with repeated times to the previous chars.
                chars, times = stack.pop()
                stack[-1][0] += (chars * times)
            else:
                stack[-1][0] += c

        return stack[0][0]


def main():
    # s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a]2[bc]"
    print Solution().decodeString(s)

    # s = "3[a2[c]]", return "accaccacc".
    s = "3[a2[c]]"
    print Solution().decodeString(s)

    # s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
    s = "2[abc]3[cd]ef"
    print Solution().decodeString(s)


if __name__ == '__main__':
    main()
