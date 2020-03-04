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
    def _add_stack(self, s):
        stack = []

        for i in range(len(s)):
            if s[i] != '#':
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()

        return stack

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool

        Time complexity: O(m+n), where
          - m: length of S
          - n: length of T.
        Space complexity: O(m+n).
        """
        # Use stack to store chars and pop by backspace.
        S_stack = self._add_stack(S)
        T_stack = self._add_stack(T)

        # Compare the remaining stacks.
        return S_stack == T_stack


class SolutionIterCharBackwards(object):
    def _getChar(self, s, pos):
        char = ''
        bs_count = 0

        while pos >= 0 and not char:
            if s[pos] == '#':
                # If char is #, increment counter.
                bs_count += 1
            elif bs_count == 0:
                # If char != # and backspace counter = 0, get char.
                char = s[pos]
            else:
                # If else, skip char and decrement counter.
                bs_count -= 1

            pos -= 1

        return char, pos

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool

        Time complexity: O(m+n).
        Space complexity: O(1).
        """
        # Visit backwards.
        S_pos, T_pos = len(S) - 1, len(T) - 1

        while S_pos >= 0 or T_pos >= 0:
            S_char, T_char = '', ''

            # Get non-backspace char.
            if S_pos >= 0:
                S_char, S_pos = self._getChar(S, S_pos)
            if T_pos >= 0:
                T_char, T_pos = self._getChar(T, T_pos)

            if S_char != T_char:
                return False

        return True


def main():
    import time

    # Output: True
    S = "ab#c"
    T = "ad#c"

    start_time = time.time()
    print 'By stack:', SolutionStack().backspaceCompare(S, T)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By backward:', SolutionIterCharBackwards().backspaceCompare(S, T)
    print 'Time:', time.time() - start_time

    # Output: True
    S = "ab##"
    T = "c#d#"

    start_time = time.time()
    print 'By stack:', SolutionStack().backspaceCompare(S, T)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By backward:', SolutionIterCharBackwards().backspaceCompare(S, T)
    print 'Time:', time.time() - start_time

    # Output: True
    S = "a##c"
    T = "#a#c"

    start_time = time.time()
    print 'By stack:', SolutionStack().backspaceCompare(S, T)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By backward:', SolutionIterCharBackwards().backspaceCompare(S, T)
    print 'Time:', time.time() - start_time

    # Output: False
    S = "bbbextm"
    T = "bbb#extm"

    start_time = time.time()
    print 'By stack:', SolutionStack().backspaceCompare(S, T)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By backward:', SolutionIterCharBackwards().backspaceCompare(S, T)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
