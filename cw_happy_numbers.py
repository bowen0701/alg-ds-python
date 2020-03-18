"""Codewars: Happy Numbers
6 kyu

URL: https://www.codewars.com/kata/59d53c3039c23b404200007e/

Math geeks and computer nerds love to anthropomorphize numbers and assign emotions and personalities
to them. Thus there is defined the concept of a "happy" number. A happy number is defined as an
integer in which the following sequence ends with the number 1.

Start with the number itself.
Calculate the sum of the square of each individual digit.
If the sum is equal to 1, then the number is happy. If the sum is not equal to 1, then repeat steps
1 and 2. A number is considered unhappy once the same number occurs multiple times in a sequence
because this means there is a loop and it will never reach 1.

For example, the number 7 is a "happy" number:
72 = 49 --> 42 + 92 = 97 --> 92 + 72 = 130 --> 12 + 32 + 02 = 10 --> 12 + 02 = 1

Once the sequence reaches the number 1, it will stay there forever since 12 = 1

On the other hand, the number 6 is not a happy number as the sequence that is generated is the following:
6, 36, 45, 41, 17, 50, 25, 29, 85, 89, 145, 42, 20, 4, 16, 37, 52, 29

Once the same number occurs twice in the sequence, the sequence is guaranteed to go on infinitely,
never hitting the number 1, since it repeat this cycle.

Your task is to write a program which will print a list of all happy numbers between 1 and x
(both inclusive), where:
2 <= x <= 5000

Disclaimer: This Kata is an adaptation of a HW assignment I had for McGill University's COMP 208 (Computers in Engineering) class.
"""

def _sum_squares(number):
    # Compute sum of squares by sum of squared digit by digit.
    result = 0
    while number > 0:
        carry, digit = number // 10, number % 10
        result += digit * digit
        number = carry
    return result


def _is_happy_number(number):
    # Use set seens to memorize seen sum of squares.
    seens = set()
    while number > 1:
        sum_squares = _sum_squares(number)
        
        # If seen sum of squares before, not happy number.
        if sum_squares in seens:
            return False
        
        # If not, add sum of squares to seen, and iterate with updating number.
        seens.add(sum_squares)
        number = sum_squares
    return True


def happy_numbers(n):
    result = []
    for number in range(1, n + 1):
        if _is_happy_number(number):
            result.append(number)
    return result


def main():
    assert happy_numbers(10) == [1, 7, 10]
    assert happy_numbers(50) == [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49]
    assert happy_numbers(100) == [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]


if __name__ == '_main__':
    main()
