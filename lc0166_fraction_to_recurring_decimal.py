"""Leetcode 166. Fraction to Recurring Decimal
Medium

URL: https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""

class SolutionRemainderPositionDict(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str

        Time complexity: O(denominator), due to mode operator %.
        Space complexity: O(1), since remainder_positions dict only takes 10.
        """
        # Note: To check repeated fractionals, just need to its 1st digit.

        if denominator == 0:
            return ''

        if numerator == 0:
            return '0'

        res = []

        # Append sign.
        if numerator / denominator < 0:
            res.append('-')

        # Convert to absoulte numerator and denominator.
        num, den = abs(numerator), abs(denominator)
        divisor, remainder = num // den, num % den

        res.append(str(divisor))

        # Only the integral part.
        if remainder == 0:
            return ''.join(res)

        res.append('.')

        # Use dict to collect remainder->1st appearance position.
        from collections import defaultdict

        remainder_positions = defaultdict(int)

        # Iteratively compute divisor & 
        while remainder != 0:
            if remainder in remainder_positions:
                # The fractional part starts recurring.
                res.insert(remainder_positions[remainder], '(')
                res.append(')')
                break
            else:
                remainder_positions[remainder] = len(res)

                next_num = remainder * 10
                divisor, remainder = next_num // den, next_num % den
                res.append(str(divisor))

        return ''.join(res)


def main():
    # Output: "0.5"
    numerator = 1
    denominator = 2
    print SolutionRemainderPositionDict().fractionToDecimal(
        numerator, denominator)

    # Output: "2"
    numerator = 2
    denominator = 1
    print SolutionRemainderPositionDict().fractionToDecimal(
        numerator, denominator)

    # Output: "0.(6)"
    numerator = 2
    denominator = 3
    print SolutionRemainderPositionDict().fractionToDecimal(
        numerator, denominator)

    # Output: "0.(571428)"
    numerator = 4
    denominator = 7
    print SolutionRemainderPositionDict().fractionToDecimal(
        numerator, denominator)

    # Output: "1.1(6)"
    numerator = 7
    denominator = 6
    print SolutionRemainderPositionDict().fractionToDecimal(
        numerator, denominator)


if __name__ == '__main__':
    main()
