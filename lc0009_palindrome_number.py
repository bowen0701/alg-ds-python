"""Leetcode 9. Palindrome Number
Easy

Determine whether an integer is a palindrome. An integer is a palindrome when 
it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 
121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        return x_str == x_str[::-1]


def main():
    x = 121  # Ans: True.
    print(Solution().isPalindrome(x))

    x = -121  # Ans: False.
    print(Solution().isPalindrome(x))

    x = 10  # Ans: False.
    print(Solution().isPalindrome(x))


if __name__ == '__main__':
    main()
