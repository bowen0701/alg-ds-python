"""Leetcode 258. Add Digits
Easy

URL: https://leetcode.com/problems/add-digits/

Given a non-negative integer num, repeatedly add all its digits until the result
has only one digit.

Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""

class SolutionIter(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int

        Time complexity: O(n), where n is number of digits in num.
        Space complexity: O(1).
        """
        num_str = str(num)

        if len(num_str) == 1:
            return num

        while len(num_str) > 1:
            new_num = 0
            for c in num_str:
                new_num += int(c)

            num_str = str(new_num)

        return new_num


def main():
    num = 38
    print SolutionIter().addDigits(num)


if __name__ == '__main__':
    main()
