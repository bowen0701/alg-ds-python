"""Leetcode 678. Valid Parenthesis String
Medium

URL: https://leetcode.com/problems/valid-parenthesis-string/

Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the
validity of a string by these rules:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single
  left parenthesis '(' or an empty string.
- An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""

class SolutionBruteForce(object):
    def _enumerate(self, s):
        """Enumerate s by replacing '*' by '(', '', & ')'."""
        s_set = set()
        queue = [s]
        while queue:
            for i in range(len(queue)):
                si = list(queue.pop())
                if si.count('*'):
                    for j, c in enumerate(si):
                        if c == '*':
                            for r in ['(', 'a', ')']:
                                si[j] = r
                                if not si.count('*'):
                                    s_set.add(''.join(si))
                                else:
                                    queue.append(''.join(si))
                else:
                    s_set.add(''.join(si))
        return list(s_set)

    def _is_valid(self, s):
        """Check s is valid with parentheses."""
        stack = []
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool

        Note: Time Limit Exceeded.

        Time complexity: O(3^k), where k is the number of '*'s.
        Space complexity: O(3^k).
        """
        # Edge case.
        if len(s) == 1:
            return s == '*'

        # Enumerate all strings with '*' replaced by, '(', '', ')'.
        s_lst = self._enumerate(s)
        print(s_lst)

        # Iterate through list to check if there is one valid.
        for si in s_lst:
            if self._is_valid(si):
                return True
        return False


def main():
    # Output: True
    s = "()"
    print(SolutionBruteForce().checkValidString(s))

    # Output: True
    s = "(*)"
    print(SolutionBruteForce().checkValidString(s))

    # Output: True
    s = "(*))"
    print(SolutionBruteForce().checkValidString(s))

    # Output: False
    s = "*(("
    print(SolutionBruteForce().checkValidString(s))

    # Output: False
    s = "**(("
    print(SolutionBruteForce().checkValidString(s))

    # Output: False
    # s = "()(()(*(())()*)(*)))()))*)((()(*(((()())()))()()*)((*)))()))(*)(()()(((()*()()((()))((*((*)()"
    # print(SolutionBruteForce().checkValidString(s))


if __name__ == '__main__':
    main()
