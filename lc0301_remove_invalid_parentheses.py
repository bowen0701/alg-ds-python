"""Leetcode 301. Remove Invalid Parentheses
Hard

URL: https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string
valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
"""

class SolutionTwoPointersDfsRecur(object):
    def _removeDfs(self, s, result, last_i, last_j, pars):
        # Increment open / decrement close counter until ')' are more.
        counter = 0
        for i in range(last_i, len(s)):
            if s[i] == pars[0]:
                counter += 1
            elif s[i] == pars[1]:
                counter -= 1
            if counter >= 0:
                continue

            # If counter < 0, remove '('.
            for j in range(last_j, len(s)):
                if s[j] == pars[1] and (j == last_j or s[j - 1] != pars[1]):
                    self._removeDfs(
                        s[:j] + s[j+1:], result, i + 1 - 1, j + 1 - 1, pars)
            return None

        # Reverse s to remove invalid '('.
        rev_s = s[::-1]

        if pars[0] == '(':
            # Finished left to right.
            self._removeDfs(rev_s, result, 0, 0, [')', '('])
        else:
            # Finished right to left.
            result.append(rev_s)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]

        Apply DFS backtracking with two pointers from head.
          - remove redundant ")" from left to right, and 
          - then remove redundant "(" from right to left.

        Time complexity: O(n*m), where
          - n: lenght of s
          - m: number of recursive calls.
        Space complexity: O(n).
        """
        if not s:
            return ['']

        # Apply DFS backtracking with two pointers from head:
        last_i, last_j = 0, 0
        pars = ['(', ')']
        result = []
        self._removeDfs(s, result, last_i, last_j, pars)
        return result


def main():
    # Output: ["()()()", "(())()"]
    s = "()())()"
    print SolutionTwoPointersDfsRecur().removeInvalidParentheses(s)

    # Output: ["(a)()()", "(a())()"]
    s = "(a)())()"
    print SolutionTwoPointersDfsRecur().removeInvalidParentheses(s)

    # Output: [""]
    s = ")("
    print SolutionTwoPointersDfsRecur().removeInvalidParentheses(s)


if __name__ == '__main__':
    main()
