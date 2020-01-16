"""Leetcode 65. Valid Number
Hard

URL: https://leetcode.com/problems/valid-number/

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
However, here is a list of characters that can be in a valid decimal number:
- Numbers 0-9
- Exponent - "e"
- Positive/negative sign - "+"/"-"
- Decimal point - "."

Of course, the context of these characters also matters in the input.
"""

class SolutionMetDigitDotEIter(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Strip s first.
        s = s.strip()

        # Iterate through char to check met digit, '.', & 'e'.
        met_digit = met_dot = met_e = False

        for i, c in enumerate(s):
            if c.isdigit():
                met_digit = True
            elif c in ['-', '+']:
                # If char is '-' or '+', and previous char is not 'e': not valid.
                if i > 0 and s[i - 1] != 'e':
                    return False
            elif c == '.':
                # If char is '.', and met '.' or 'e' before: not valid.
                # O.w. mark met '.'
                if met_dot or met_e:
                    return False
                met_dot = True
            elif c == 'e':
                # If char is 'e', and met 'e' or not met digit before: not valid. 
                # O.w. mark met 'e' and not met digit.
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False
            else:
                # O.w.: not valid.
                return False

        return met_digit


def main():
    # "0" => true
    print SolutionMetDigitDotEIter().isNumber('0')

    # " 0.1 " => true
    print SolutionMetDigitDotEIter().isNumber(' 0.1 ')

    # "abc" => false
    print SolutionMetDigitDotEIter().isNumber('abc')

    # "1 a" => false
    print SolutionMetDigitDotEIter().isNumber('1 a')

    # "2e10" => true
    print SolutionMetDigitDotEIter().isNumber('2e10')

    # " -90e3   " => true
    print SolutionMetDigitDotEIter().isNumber(' -90e3   ')

    # " 1e" => false
    print SolutionMetDigitDotEIter().isNumber(' 1e')

    # "e3" => false
    print SolutionMetDigitDotEIter().isNumber('e3')

    # " 6e-1" => true
    print SolutionMetDigitDotEIter().isNumber(' 6e-1')

    # " 99e2.5 " => false
    print SolutionMetDigitDotEIter().isNumber(' 99e2.5 ')

    # "53.5e93" => true
    print SolutionMetDigitDotEIter().isNumber('53.5e93')

    # " --6 " => false
    print SolutionMetDigitDotEIter().isNumber(' --6 ')

    # "-+3" => false
    print SolutionMetDigitDotEIter().isNumber('-+3')

    # "95a54e53" => false
    print SolutionMetDigitDotEIter().isNumber('95a54e53')


if __name__ == '__main__':
    main()
