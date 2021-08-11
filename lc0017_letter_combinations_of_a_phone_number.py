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

from typing import List


class SolutionListComprehension(object):
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time complexity: O(n*m^2)
          - n is the length of digits,
          - m is the mean length of digit's letters, basically 3.
        Space complexity: O(m^n).
        """
        # Create dict:digit->list(letters).
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
        
        # Edge cases.
        if not digits:
            return []
        if len(digits) == 1:
            return d2l_d[digits]

        # Initialize result by digits's 1st letters.
        result = d2l_d[digits[0]]

        # Iterate through digits to combine result and letters.
        for i in range(1, len(digits)):
            letters_i = d2l_d[digits[i]]
            result = [m + n for m in result for n in letters_i]
        
        return result


class SolutionDFSRecur(object):
    def _dfsRecur(self, result: List[str], digits: str, cur_str: str, i: int):
        # If index is out of boundary, complete combination.
        if i == len(digits):
            result.append(cur_str)
            return None

        # Iterate through letters to apply DFS.
        letters_i = self.d2l_d[digits[i]]
        for l in letters_i:
            self._dfsRecur(result, digits, cur_str + l, i + 1)

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time complexity: O(n*m^2)
          - n is the length of digits,
          - m is the mean length of digit's letters, basically 3.
        Space complexity: O(m^n).
        """
        # Create dict:digit->list(letter).
        self.d2l_d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k' ,'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if not digits:
            return []
        if len(digits) == 1:
            return self.d2l_d[digits]

        # Apply recursive DFS.
        result = []
        cur_str = ''
        i = 0
        self._dfsRecur(result, digits, cur_str, i)
        return result


def main():
    import time

    # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    digits =  "23"

    start_time = time.time()
    print('By list comp:', SolutionListComprehension().letterCombinations(digits))
    print('Time:', time.time() - start_time)

    start_time = time.time()
    print('By DFS recur', SolutionDFSRecur().letterCombinations(digits))
    print('Time:', time.time() - start_time)


if __name__ == '__main__':
    main()
