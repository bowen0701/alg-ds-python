"""Leetcode 38. Count and Say
Easy

URL: https://leetcode.com/problems/count-and-say/

The count-and-say sequence is the sequence of integers with the 
first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 <= n <= 30, generate the nth term of the 
count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''

        res = '1'

        for _ in range(n - 1):
            # Start from the 1st digit.
            digit = res[0]
            temp = ''
            count = 0

            # Iterate through all digits.
            for d in res:
                if digit == d:
                    # If current digit is equal to digit, increment count.
                    count += 1
                else:
                    # If not, append count+digit string.
                    temp += str(count) + digit
                    # Update digit to current digit with new count = 1.
                    digit = d
                    count = 1
            
            # Append the last count+digit string to res.
            temp += str(count) + digit
            res = temp

        return res


def main():
    n = 5
    print Solution().countAndSay(n)


if __name__ == '__main__':
    main()
