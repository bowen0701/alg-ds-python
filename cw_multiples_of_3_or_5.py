"""Codewars: Multiples of 3 or 5
6 kyu

URL: https://www.codewars.com/kata/514b92a657cdc65150000006/

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5
below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once.
"""


def solution(number):
    """
    Time complexity: O(n), where n is number.
    Space complexity: O(1).
    """
    result = 0
    for n in range(1, number):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    return result


def main():
    assert solution(10) == 23
    assert solution(16) == 60


if __name__ == '__main__':
    main()
