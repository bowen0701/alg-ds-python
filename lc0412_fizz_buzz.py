"""Leetcode 412. Fizz Buzz
Easy

URL: https://leetcode.com/problems/fizz-buzz/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output "Fizz" instead of the number and
for the multiples of five output "Buzz".
For numbers which are multiples of both three and five output "FizzBuzz".

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzbuzz = [None] * n

        for i in range(1, n + 1):
            if i % 15 == 0:
                fizzbuzz[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                fizzbuzz[i - 1] = "Fizz"
            elif i % 5 == 0:
                fizzbuzz[i - 1] = "Buzz"
            else:
                fizzbuzz[i - 1] = str(i)

        return fizzbuzz


def main():
    n = 15
    print Solution().fizzBuzz(n)


if __name__ == '__main__':
    main()
