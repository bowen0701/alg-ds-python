"""Leetcode 22. Generate Parentheses
Medium

URL: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate 
all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class SolutionRecur(object):
    def _parenthesisRecur(self, n_opens, n_closes, result, temp):
        if n_opens == 0 and n_closes == 0:
            # If there are no left/right parentheses, append temp.
            result.append(temp)
            return None

        if n_opens > 0:
            # If there is left parentheses, use one left.
            self._parenthesisRecur(n_opens - 1, n_closes, result, temp + '(')

        if n_opens < n_closes:
            # If number of left parentheses is less than of right, use one right.
            self._parenthesisRecur(n_opens, n_closes - 1, result, temp + ')')

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        Time complexity: O((2n)!/(n!*n!)/(1/(1+n))).
        Space complexity: O(n).
        """
        n_opens, n_closes = n, n
        result = []
        temp = ''
        self._parenthesisRecur(n_opens, n_closes, result, temp)
        return result


def main():
    n = 3
    print SolutionRecur().generateParenthesis(n)


if __name__ == '__main__':
    main()
