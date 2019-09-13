"""Leetcode 17. Letter Combinations of a Phone Number
Medium

URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible 
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is 
given below. Note that 1 does not map to any letters.
{
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, 
your answer could be in any order you want.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
 
        Time complexity: O(n * m^2)
          - n is the length of digits,
          - m is the mean length of digit's letters, basically 3.
        Space complexity: O(m^n).
        """
        # Store digit->letter-list dict.
        d2l_d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k' ,'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        # Edge cases handling.
        if not digits:
            return []
        if len(digits) == 1:
            return d2l_d[digits]

        # Initialize output lc by the 0th digit's letter-list.
        lc = d2l_d[digits[0]]

        # Run for loop over digits starting from index i = 1.
        #   - Get the ith digit's letter list li.
        #   - Use list comprehension to combine lc and li to replace lc.
        for i in range(1, len(digits)):
            li = d2l_d[digits[i]]
            lc = [m + n for m in lc for n in li]
        
        return lc


def main():
    digits =  "23"
    # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    print Solution().letterCombinations(digits)


if __name__ == '__main__':
    main()
