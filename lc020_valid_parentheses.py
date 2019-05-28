"""Leetcode 20. Valid Parentheses
Easy

URL: https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Make a open->close brackets dict.
        open_close_d = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []
        for c in s:
            # If c is open bracket, push to stack.
            if c in '([{':
                stack.append(c)
                continue
            # If c in close bracket, pop element from stack and check match.
            if c in ')]}':
                # If no open bracket in stack, we have non-matched close one.
                if not stack:
                    return False
                open_c = stack.pop()
                if open_close_d.get(open_c) != c:
                    return False

        # Check whether there is non-matched open bracket.
        if not stack:
            return True
        else:
            return False


def main():
    # Input: "()"
    # Output: true
    s = '()'
    print Solution().isValid(s)

    # Input: "()[]{}"
    # Output: true
    s = '()[]{}'
    print Solution().isValid(s)

    # Input: "(]"
    # Output: false
    s = '(]'
    print Solution().isValid(s)

    # Input: "([)]"
    # Output: false
    s = '([)]'
    print Solution().isValid(s)

    # Input: "{[]}"
    # Output: true
    s = '{[]}'
    print Solution().isValid(s)

    # Input: '['
    # Output: False
    s = '['
    print Solution().isValid(s)

    # Input: ']'
    # Output: False
    s = ']'
    print Solution().isValid(s)


if __name__ == '__main__':
    main()
