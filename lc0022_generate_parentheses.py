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
    def _parenthesisRecur(self, n_lefts, n_rights, 
                          acc_string, parentheses):
        if n_lefts == 0 and n_rights == 0:
            # If there are no left/right parentheses, append acc_string.
            parentheses.append(acc_string)
            return

        if n_lefts > 0:
            # If there is left parentheses, use one left.
            self._parenthesisRecur(n_lefts - 1, n_rights, 
                                   acc_string + '(', parentheses)

        if n_lefts < n_rights:
            # If number of left parentheses is less than of right, use one right.
            self._parenthesisRecur(n_lefts, n_rights - 1, 
                                   acc_string + ')', parentheses)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        Time complexity: O((2n)!/(n!*n!)/(1/(1+n))).
        Space complexity: O(n).
        """
        parentheses = []
        self._parenthesisRecur(n, n, '', parentheses)
        return parentheses


def main():
    n = 3
    print SolutionRecur().generateParenthesis(n)


if __name__ == '__main__':
    main()
