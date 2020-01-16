"""Leetcode 921. Minimum Add to Make Parentheses Valid
Medium

Given a string S of '(' and ')' parentheses, we add the minimum number of 
parentheses ( '(' or ')', and in any positions ) so that the resulting 
parentheses string is valid.

Formally, a parentheses string is valid if and only if:
- It is the empty string, or
- It can be written as AB (A concatenated with B), where A and B are valid 
strings, or
- It can be written as (A), where A is a valid string.

Given a parentheses string, return the minimum number of parentheses we must 
add to make the resulting string valid.

Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4

Note:
S.length <= 1000
S only consists of '(' and ')' characters.
"""

class SolutionStackEmptyIncrementCount(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int

        Time complexity: O(n), where n is the length of S.
        Space complexity: O(n).
        """
        count = 0
        stack = []

        for c in S:
            if c == '(':
                # Append left parenthesis to stack.
                stack.append(c)
            elif stack:
                # If right parenthesis and not empty stack, pop stack.
                stack.pop()
            else:
                # If right parenthesis and empty stack. Count extra right ones.
                count += 1

        # Count the remaining left stack.
        count += len(stack)

        return count


def main():
    S = '(())'  # Ans: 0.
    print(SolutionStackEmptyIncrementCount().minAddToMakeValid(S))

    S = '())'  # Ans: 1.
    print(SolutionStackEmptyIncrementCount().minAddToMakeValid(S))

    S = '((('  # Ans: 3.
    print(SolutionStackEmptyIncrementCount().minAddToMakeValid(S))

    S = '()'  # Ans: 0.
    print(SolutionStackEmptyIncrementCount().minAddToMakeValid(S))

    S = '()))((' # Ans: 4.
    print(SolutionStackEmptyIncrementCount().minAddToMakeValid(S))


if __name__ == '__main__':
    main()
