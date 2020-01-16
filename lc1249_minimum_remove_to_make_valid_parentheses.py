"""Leetcode 1249. Minimum Remove to Make Valid Parentheses
Medium

URL: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')',
in any positions ) so that the resulting parentheses string is valid and
return any valid string.

Formally, a parentheses string is valid if and only if:
- It is the empty string, contains only lowercase characters, or
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

Constraints:
- 1 <= s.length <= 10^5
- s[i] is one of  '(' , ')' and lowercase English letters.
"""


class SolutionStackAppendValidChars(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Iterate through chars, add valid chars to valid chars array.
        LOWER_CHARS = 'abcdefghijklmnopqrstuvwxyz'
        stack = []
        valid_chars = []

        for c in s:
            if c == '(' or c in LOWER_CHARS:
                # If char is '(' or lower, add char to valid chars.
                valid_chars.append(c)

                if c == '(':
                    # If '(', push it to stack.
                    stack.append('(')

            elif c == ')' and stack:
                # If char is ')' and stack contains ')' for matching,
                # add char to valid chars and pop '('.
                valid_chars.append(c)
                stack.pop()
            else:
                # If not match, ignore ')' and continue.
                continue

        if stack:
            # If there remain '(', remove redundant '(' by its number from backward.
            counter = len(stack)
            for i in range(len(valid_chars) - 1, -1, -1):
                if counter > 0:
                    if valid_chars[i] == '(':
                        valid_chars[i] = ''
                        counter -= 1
                else:
                    break
        
        return ''.join(valid_chars)


def main():
    # Output: "lee(t(c)o)de"
    s = "lee(t(c)o)de)"
    print SolutionStackAppendValidChars().minRemoveToMakeValid(s)

    # Output: "ab(c)d"
    s = "a)b(c)d"
    print SolutionStackAppendValidChars().minRemoveToMakeValid(s)

    # Output: ""
    s = "))(("
    print SolutionStackAppendValidChars().minRemoveToMakeValid(s)

    # Output: "a(b(c)d)"
    s = "(a(b(c)d)"
    print SolutionStackAppendValidChars().minRemoveToMakeValid(s)

    # Output: "()()"
    s = "())()((("
    print SolutionStackAppendValidChars().minRemoveToMakeValid(s)


if __name__ == '__main__':
    main()
