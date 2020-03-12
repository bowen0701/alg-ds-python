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

class SolutionListComprehension(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
 
        Time complexity: O(n*m^2)
          - n is the length of digits,
          - m is the mean length of digit's letters, basically 3.
        Space complexity: O(m^n).
        """
        # Create dict:digit->list(letters).
        dtol_d = {
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
            return dtol_d[digits]

        # Initialize output letters by the 0th digit's letters.
        letters = dtol_d[digits[0]]

        # Iterate through digits starting from i = 1, 
        # replace letters by combining letters and letters_i.
        for i in range(1, len(digits)):
            letters_i = dtol_d[digits[i]]
            letters = [m + n for m in letters for n in letters_i]
        
        return letters


class SolutionDFSRecur(object):
    def _dfsRecur(self, letters, digits, dtol_d, cur_str, idx):
        # If idx is out of boundary, complete combination.
        if idx == len(digits):
            letters.append(cur_str)
            return None

        # Iterate through letters at digit i.
        letters_idx = dtol_d[digits[idx]]
        for letter in letters_idx:
            # Apply DFS to append letter and increment index.
            self._dfsRecur(letters, digits, dtol_d, cur_str + letter, idx + 1)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
 
        Time complexity: O(n*m^2)
          - n is the length of digits,
          - m is the mean length of digit's letters, basically 3.
        Space complexity: O(m^n).
        """
        # Create dict:digit->list(letter).
        dtol_d = {
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
            return dtol_d[digits]

        # Apply recursive DFS.
        letters = []
        cur_str = ''
        idx = 0
        self._dfsRecur(letters, digits, dtol_d, cur_str, idx)
        return letters


def main():
    import time

    # Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    digits =  "23"

    start_time = time.time()
    print 'By list comp:', SolutionListComprehension().letterCombinations(digits)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'By BFS recur', SolutionDFSRecur().letterCombinations(digits)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
