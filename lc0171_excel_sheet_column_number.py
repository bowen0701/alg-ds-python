"""Leetcode 171. Excel Sheet Column Number
Easy

URL: https://leetcode.com/problems/excel-sheet-column-number/

Given a column title as appear in an Excel sheet,
return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n), where n is the lenght of s.
        Space complexity: O(1).
        """
        base = 26
        num = 0

        for i, c in enumerate(reversed(s)):
            current_num = ord(c) - ord('A') + 1
            num += pow(base, i) * current_num

        return num


def main():
    s = 'A'
    print Solution().titleToNumber(s)

    s = 'AB'
    print Solution().titleToNumber(s)

    s = 'ZY'
    print Solution().titleToNumber(s)


if __name__ == '__main__':
    main()
