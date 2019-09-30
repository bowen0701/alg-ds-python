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
    def _parenthesisRecur(self, n_opens, n_closes, 
                          cur_string, parentheses):
        if n_opens == 0 and n_closes == 0:
            # If there are no left/right parentheses, append cur_string.
            parentheses.append(cur_string)
            return

        if n_opens > 0:
            # If there is left parentheses, use one left.
            self._parenthesisRecur(n_opens - 1, n_closes, 
                                   cur_string + '(', parentheses)

        if n_opens < n_closes:
            # If number of left parentheses is less than of right, use one right.
            self._parenthesisRecur(n_opens, n_closes - 1, 
                                   cur_string + ')', parentheses)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        Time complexity: O((2n)!/(n!*n!)/(1/(1+n))).
        Space complexity: O(n).
        """
        parentheses = []
        n_opens, n_closes = n, n
        cur_string = ''
        self._parenthesisRecur(n_opens, n_closes, cur_string, parentheses)
        return parentheses


def main():
    n = 3
    print SolutionRecur().generateParenthesis(n)


if __name__ == '__main__':
    main()
