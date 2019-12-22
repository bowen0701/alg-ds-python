"""Leetcode 796. Rotate String
Easy

URL: https://leetcode.com/problems/rotate-string/

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to
the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
after one shift on A. Return True if and only if A can become B after some
number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

Note:
A and B will have length at most 100.
"""

class SolutionStringConcatSubstring(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool

        Time complexity: O(2n+2n*n)=O(n^2).
        Space complexity:O(n).
        """
        # Check if lengths are not equal.
        if len(A) != len(B):
            return False

        # If rotate string, B is substring of concated string A + A.
        AA = A + A
        if B in AA:
            return True
        else:
            return False


def main():
    # Input: A = 'abcde', B = 'cdeab'
    # Output: true
    A = 'abcde'
    B = 'cdeab'
    print SolutionStringConcatSubstring().rotateString(A, B)

    # Input: A = 'abcde', B = 'abced'
    # Output: false
    A = 'abcde'
    B = 'abced'
    print SolutionStringConcatSubstring().rotateString(A, B)


if __name__ == '__main__':
    main()
