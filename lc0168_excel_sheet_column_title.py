"""Leetcode 168. Excel Sheet Column Title
Easy

URL: https://leetcode.com/problems/excel-sheet-column-title/

Given a positive integer, return its corresponding column title as appear
in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
"""

class SolutionRemStack(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Use stack to collect iterative remainders of n % 26.
        rem_stack = []

        while n:
            # Since we use rem + ord('A'), decrement n by 1 first.
            n -= 1
            rem = n % 26
            rem_stack.append(chr(rem + ord('A')))

            n //= 26

        # Reversely concat letters.
        return ''.join(rem_stack[::-1])


def main():
    # Output: "A"
    n = 1
    print SolutionRemStack().convertToTitle(n)

    # Output: "AB"
    n = 28
    print SolutionRemStack().convertToTitle(n)

    # Output: "ZY"
    n = 701
    print SolutionRemStack().convertToTitle(n)

    # Output: "Z"
    n = 26
    print SolutionRemStack().convertToTitle(n)

    # Output: "AZ"
    n = 52
    print SolutionRemStack().convertToTitle(n)


if __name__ == '__main__':
    main()
