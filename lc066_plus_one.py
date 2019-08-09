"""Leetcode 66. Plus One
Easy

URL: https://leetcode.com/problems/plus-one/

Given a non-empty array of digits representing a non-negative integer, 
plus one to the integer.

The digits are stored such that the most significant digit is at the 
head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Time complexity: O(n), where n is the length of digits.
        Space complexity: O(n), for worse case of total overflow.
        """
        overflow = False

        # Start from the last digit and reverse back to the 1st one.
        for i in reversed(range(len(digits))):
            # Plus one only for the last digit or when overflow.
            if overflow or i == len(digits) - 1: 
                if digits[i] + 1 < 10:
                    digits[i] += 1
                    return digits
                else:
                    overflow = True
                    digits[i] = 0

        # If there is total overflow, plus to the head of digits.
        if overflow:
            digits.insert(0, 1)
        return digits


def main():
    # Ans: [1,2,4]
    digits = [1,2,3]
    print Solution().plusOne(digits)

    # Ans: [4,3,2,2] 
    digits = [4,3,2,1]
    print Solution().plusOne(digits)

    # Ans: [3, 0]
    digits = [2, 9]
    print Solution().plusOne(digits)

    # Ans: [1, 0, 0]
    digits = [9, 9]
    print Solution().plusOne(digits)


if __name__ == '__main__':
    main()
