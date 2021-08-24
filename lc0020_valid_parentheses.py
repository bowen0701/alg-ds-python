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

class SolutionOpenCloseDictOpenStack(object):
    def isValid(self, s: str) -> bool:
        """
        Time complexity: O(n), where n is the length of the string.
        Space complexity: O(n).
        """
        # Make a open->close brackets dict.
        open_close_d = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        open_set = set('([{')
        close_set = set(')]}')

        # Use stack to check valid parentheses.
        stack = []

        for c in s:
            # If c is open parenthesis, push to stack.
            if c in open_set:
                stack.append(c)
                continue

            # If c in close bracket.
            if c in close_set:
                # Check if there is still open parenthesis.
                if not stack:
                    return False

                # If yes, pop & compare open parenthesis and current char.
                o = stack.pop()
                if open_close_d[o] != c:
                    return False

        # Check if there is still open remaining.
        if not stack:
            return True
        else:
            return False


def main():
    # Input: "()"
    # Output: true
    s = '()'
    print(SolutionOpenCloseDictOpenStack().isValid(s))

    # Input: "()[]{}"
    # Output: true
    s = '()[]{}'
    print(SolutionOpenCloseDictOpenStack().isValid(s))

    # Input: "(]"
    # Output: false
    s = '(]'
    print(SolutionOpenCloseDictOpenStack().isValid(s))

    # Input: "([)]"
    # Output: false
    s = '([)]'
    print(SolutionOpenCloseDictOpenStack().isValid(s))

    # Input: "{[]}"
    # Output: true
    s = '{[]}'
    print(SolutionOpenCloseDictOpenStack().isValid(s))

    # Input: '['
    # Output: False
    s = '['
    print(SolutionOpenCloseDictOpenStack().isValid(s))

    # Input: ']'
    # Output: False
    s = ']'
    print(SolutionOpenCloseDictOpenStack().isValid(s))


if __name__ == '__main__':
    main()
