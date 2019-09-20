"""Leetcode 844. Backspace String Compare
Easy

URL: https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
- 1 <= S.length <= 200
- 1 <= T.length <= 200
- S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
"""

class SolutionStack(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool

        Time complexity: O(max(m, n)), where
          - m: length of S
          - n: length of T.
        Space complexity: O(max(m, n)).
        """
        # Use stack to store chars and pop by backspace.
        S_stack = []
        T_stack = []

        for i in range(len(S)):
            if S[i] != '#':
                S_stack.append(S[i])
            else:
                if S_stack:
                    S_stack.pop()

        for i in range(len(T)):
            if T[i] != '#':
                T_stack.append(T[i])
            else:
                if T_stack:
                    T_stack.pop()

        # Compare the remaining stack.
        if len(S_stack) != len(T_stack):
            return False

        for i in range(len(S_stack)):
            if S_stack[i] != T_stack[i]:
                return False

        return True


def main():
    # Output: True
    S = "ab#c"
    T = "ad#c"
    print SolutionStack().backspaceCompare(S, T)

    # Output: True
    S = "ab##"
    T = "c#d#"
    print SolutionStack().backspaceCompare(S, T)

    # Output: True
    S = "a##c"
    T = "#a#c"
    print SolutionStack().backspaceCompare(S, T)

    # Output: False
    S = "a#c"
    T = "b"
    print SolutionStack().backspaceCompare(S, T)


if __name__ == '__main__':
    main()
