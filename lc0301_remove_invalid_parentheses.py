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
    def _removeDfs(self, s, result, last_i, last_j, open_par, close_par):
        # Accumulate parentheses match until close ones are more. 
        count = 0
        i = last_i
        while i < len(s) and count >= 0:
            if s[i] == open_par:
                count += 1
            if s[i] == close_par:
                count -= 1

            i += 1

        if count >= 0:
            # No extrac ')' is detected, now detect extra '(' by reversing string.
            rev_s = s[::-1]

            if open_par == '(':
                # Start removing '(' from reversed string by DFS.
                self._removeDfs(rev_s, result, 0, 0, ')', '(')
            else:
                # Finished removing '(', append the original string to result.
                result.append(rev_s)
        else:
            # Get the index of abnormal ')' which makes count < 0: i - 1.
            i -= 1
            j = last_j
            while j <= i:
                if s[j] == close_par and (j == last_j or s[j - 1] != close_par):
                    # After removal, the prefix is valid. Then recursively remove the rest of the string.
                    # New last_i is i + 1 - 1, due to removal; similarly with last_j.
                    # To avoid duplicates, only remove the 1st ')'.
                    self._removeDfs(s[:j] + s[j+1:], result, i, j, open_par, close_par)
                
                j += 1

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [s]

        result = []
        # Two poinsters: Use last_i to denote last char we checked, last_j we removed.
        last_i = 0
        last_j = 0
        open_par = '('
        close_par = ')'
        self._removeDfs(s, result, last_i, last_j, open_par, close_par)
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
