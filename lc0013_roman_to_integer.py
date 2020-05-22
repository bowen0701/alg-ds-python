"""Leetcode 13. Roman to Integer
Easy

URL: https://leetcode.com/problems/roman-to-integer/

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

class SolutionSubtractRules(object):
    def _get_roman_to_value(self, i, roman):
        # If roman is I, X or C, check its next roman to decide subtract or add.
        if ((roman == 'I' and self.s[i + 1] in ['V', 'X'])
            or (roman == 'X' and self.s[i + 1] in ['L', 'C'])
            or (roman == 'C' and self.s[i + 1] in ['D', 'M'])):
            return -self.roman2int_d[roman]
        else:
            return self.roman2int_d[roman]

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n), where n is the length of s.
        Space complexity: O(1), which is the size of roman to integer dict.
        """
        self.s = s
        n = len(self.s)

        # Create a dict:roman->int.
        self.roman2int_d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # For each roman, get its value by rules and add it to result.
        result = 0
        for i, roman in enumerate(s):
            if i < n - 1:
                result += self._get_roman_to_value(i, roman)
            else:
                result += self.roman2int_d[roman]
        return result


class SolutionLeftBigger(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n), where n is the length of s.
        Space complexity: O(1), which is the size of roman to integer dict.
        """
        n = len(s)

        # Create a dict:roman->int.
        roman2int_d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Check if right's int is bigger, subtract, o.w. add to result.
        result = 0
        for i in range(n - 1):
            if roman2int_d[s[i]] < roman2int_d[s[i + 1]]:
                result -= roman2int_d[s[i]]
            else:
                result += roman2int_d[s[i]]
        result += roman2int_d[s[n - 1]]
        return result


class SolutionReplace(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int

        Time complexity: O(??).
        Space complexity: O(??).
        """
        pass


def main():
    import time

    print 'By SolutionSubtractRules:'
    start_time = time.time()
    s = 'III'  # Output: 3.
    print SolutionSubtractRules().romanToInt(s)
    s = 'IV'  # Output: 4.
    print SolutionSubtractRules().romanToInt(s)
    s = 'IX'  # Output: 9.
    print SolutionSubtractRules().romanToInt(s)
    s = 'LVIII'  # Output: 58.
    print SolutionSubtractRules().romanToInt(s)
    s = 'MCMXCIV'  # Output: 1994.
    print SolutionSubtractRules().romanToInt(s)
    print 'Time: {}'.format(time.time() - start_time)

    print 'By SolutionLeftBigger:'
    start_time = time.time()
    s = 'III'  # Output: 3.
    print SolutionLeftBigger().romanToInt(s)
    s = 'IV'  # Output: 4.
    print SolutionLeftBigger().romanToInt(s)
    s = 'IX'  # Output: 9.
    print SolutionLeftBigger().romanToInt(s)
    s = 'LVIII'  # Output: 58.
    print SolutionLeftBigger().romanToInt(s)
    s = 'MCMXCIV'  # Output: 1994.
    print SolutionLeftBigger().romanToInt(s)
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
