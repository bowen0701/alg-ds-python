"""Leetcode 13. Roman to Integer
Easy

Roman numerals are represented by seven different symbols: 
I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, 
just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. 
Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Example 3:
Input: "IX"
Output: 9

Example 4:
Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

class Solution(object):
    def __init__(self):
        # Create a Roman to int dictionary.
        self.roman2int_d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def numeral_to_int(self, i, rn):
        # If rn is I, X or C, check its next rn.
        # If the rn and its next rn do not specify an number,
        # just add rn's int to integer; if yes, substract int from integer.
        if rn == 'I':
            if i + 1 < len(self.s) and self.s[i + 1] in ['V', 'X']:
                return -self.roman2int_d[rn]
            else:
                return self.roman2int_d[rn]
        elif rn == 'X':
            if i + 1 < len(self.s) and self.s[i + 1] in ['L', 'C']:
                return -self.roman2int_d[rn]
            else:
                return self.roman2int_d[rn]
        elif rn == 'C':
            if i + 1 < len(self.s) and self.s[i + 1] in ['D', 'M']:
                return -self.roman2int_d[rn]
            else:
                return self.roman2int_d[rn]
        else:
            return self.roman2int_d[rn]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n), where n is the length of s.
        Space complexity: O(1), which is the size of roman to integer dict.
        """
        self.s = s
        integer = 0

        # For each Roman numeral rn, get its int value and add to integer.
        for i, rn in enumerate(s):
            integer += self.numeral_to_int(i, rn)

        return integer


def main():
    s = 'III'  # Output: 3.
    print Solution().romanToInt(s)

    s = 'IV'  # Output: 4.
    print Solution().romanToInt(s)

    s = 'IX'  # Output: 9.
    print Solution().romanToInt(s)

    s = 'LVIII'  # Output: 58.
    print Solution().romanToInt(s)

    s = 'MCMXCIV'  # Output: 1994.
    print Solution().romanToInt(s)


if __name__ == '__main__':
    main()
