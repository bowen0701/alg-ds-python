"""Leetcode 6. ZigZag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number 
of rows like this: (you may want to display this pattern in a fixed font for 
better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a 
number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I     N
A   L S   I G
Y A   H R
P     I
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s

        zigzag_rows = ['' for _ in range(numRows)]
        row = 0
        for x in s:
            zigzag_rows[row] += x
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(zigzag_rows)


class SolutionMath(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows or numRows == 1:
            return s

        len_s = len(s)
        base = (numRows - 1) * 2

        zigzag = ''
        for r in range(numRows):
            if r == 0:             # First row.
                for i in range(0, len_s, base):
                    zigzag += s[i]
            elif r == numRows - 1: # Last row.
                for i in range(r, len_s, base):
                    zigzag += s[i]
            else:                  # Middle rows.
                for i in range(r, len_s, base):
                    zigzag += s[i]
                    if i + (base - 2 * r) < len_s:
                        zigzag += s[i + (base - 2 * r)]
        return zigzag


def main():
    s = "PAYPALISHIRING"

    numRows = 3
    zigzag = Solution().convert(s, numRows)
    print zigzag
    assert zigzag == 'PAHNAPLSIIGYIR'

    numRows = 4
    zigzag = Solution().convert(s, numRows)
    print zigzag
    assert zigzag == 'PINALSIGYAHRPI'

    numRows = 3
    zigzag = SolutionMath().convert(s, numRows)
    print zigzag
    assert zigzag == 'PAHNAPLSIIGYIR'

    numRows = 4
    zigzag = SolutionMath().convert(s, numRows)
    print zigzag
    assert zigzag == 'PINALSIGYAHRPI'

    s = "PAYPALISHIRING"

    numRows = 3
    zigzag = Solution().convert(s, numRows)
    print zigzag
    assert zigzag == 'PAHNAPLSIIGYIR'

    numRows = 3
    zigzag = SolutionMath().convert(s, numRows)
    print zigzag
    assert zigzag == 'PAHNAPLSIIGYIR'


if __name__ == '__main__':
    main()
