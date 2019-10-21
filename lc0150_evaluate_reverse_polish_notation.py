"""Leetcode 150. Evaluate Reverse Polish Notation
Medium

URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
- Division between two integers should truncate toward zero.
- The given RPN expression is always valid. That means the expression would always
  evaluate to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

class SolutionStack(object):
    def _arithmetic_ops(self, x1, x2, op):
        if op == '+':
            return x1 + x2
        elif op == '-':
            return x1 - x2
        elif op == '*':
            return x1 * x2
        elif op == '/':
            if x1 * x2 < 0 and x1 % x2 != 0:
                # If one of two numbers is negative, and abs(x1) < abs(x2).
                return x1 // x2 + 1
            else:
                return x1 // x2

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int

        Apply stack to store numbers, iterate through the tokens,
        and pop two numbers for arithmetic operation token.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        stack = []

        for t in tokens:
            if t not in set(['+', '-', '*', '/']):
                stack.append(int(t))
            else:
                x2 = stack.pop()
                x1 = stack.pop()
                res = self._arithmetic_ops(x1, x2, t)
                stack.append(res)

        return stack[0]


def main():
    # Output: 9
    tokens = ["2", "1", "+", "3", "*"]
    print SolutionStack().evalRPN(tokens)

    # Output: 6
    tokens = ["4", "13", "5", "/", "+"]
    print SolutionStack().evalRPN(tokens)

    # Output: 22
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print SolutionStack().evalRPN(tokens)


if __name__ == '__main__':
    main()
