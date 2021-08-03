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

from typing import List, Tuple


class SolutionStack(object):
    def _add_stack(self, s: str) -> List[str]:
        stack = []

        for i in range(len(s)):
            if s[i] != '#':
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()

        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Time complexity: O(m+n), where
          - m: length of S
          - n: length of T.
        Space complexity: O(m+n).
        """
        # Use stack to store chars and pop by backspace.
        s_stack = self._add_stack(s)
        t_stack = self._add_stack(t)

        # Compare the remaining stacks.
        return s_stack == t_stack


class SolutionIterCharBackwards(object):
    def _getChar(self, s: str, pos: int) -> Tuple[str, int]:
        char = ''
        n_backspaces = 0

        while pos >= 0 and not char:
            if s[pos] == '#':
                # If char is #, increment counter.
                n_backspaces += 1
            elif n_backspaces == 0:
                # If char != # and backspace counter = 0, get char.
                char = s[pos]
            else:
                # If else, skip char and decrement counter.
                n_backspaces -= 1

            pos -= 1

        return char, pos

    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Time complexity: O(m+n).
        Space complexity: O(1).
        """
        # Visit backwards.
        s_pos, t_pos = len(s) - 1, len(t) - 1

        while s_pos >= 0 or t_pos >= 0:
            s_char, t_char = '', ''

            # Get non-backspace char.
            if s_pos >= 0:
                s_char, s_pos = self._getChar(s, s_pos)
            if t_pos >= 0:
                t_char, t_pos = self._getChar(t, t_pos)

            if s_char != t_char:
                return False

        return True


def main():
    import time

    # Output: True
    s = "ab#c"
    t = "ad#c"

    start_time = time.time()
    print('By stack:', SolutionStack().backspaceCompare(s, t))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By backward:', SolutionIterCharBackwards().backspaceCompare(s, t))
    print('Time:', time.time() - start_time)

    # Output: True
    s = "ab##"
    t = "c#d#"

    start_time = time.time()
    print('By stack:', SolutionStack().backspaceCompare(s, t))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By backward:', SolutionIterCharBackwards().backspaceCompare(s, t))
    print('Time:', time.time() - start_time)

    # Output: True
    s = "a##c"
    t = "#a#c"

    start_time = time.time()
    print('By stack:', SolutionStack().backspaceCompare(s, t))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By backward:', SolutionIterCharBackwards().backspaceCompare(s, t))
    print('Time:', time.time() - start_time)

    # Output: False
    s = "bbbextm"
    t = "bbb#extm"

    start_time = time.time()
    print('By stack:', SolutionStack().backspaceCompare(s, t))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By backward:', SolutionIterCharBackwards().backspaceCompare(s, t))
    print('Time:', time.time() - start_time)


if __name__ == '__main__':
    main()
