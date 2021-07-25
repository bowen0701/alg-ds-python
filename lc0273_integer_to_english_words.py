"""Leetcode 273. Integer to English Words
Hard

URL: https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
Thousand Eight Hundred Ninety One"
"""

from typing import List


class SolutionLessThan20TensPowersOfThousandsRecur(object):
    def _getWordsRecur(self, num: int) -> List[str]:
        # Return empty array for exact matched case.
        if not num:
            return []

        if num < 20:
            return [self.lessThan20[num - 1]]

        if num < 100:
            return [self.tens[num // 10 - 1]] + self._getWordsRecur(num % 10)

        if num < 1000:
            return ([self.lessThan20[num // 100 - 1]] 
                     + ['Hundred'] 
                     + self._getWordsRecur(num % 100))

        for p, word in enumerate(self.powersOfThousand, start=1):
            # Convert top-bottom by finding the largest power of thousand.
            if num < 1000 ** (p + 1):
                return (self._getWordsRecur(num // (1000 ** p)) 
                        + [word] 
                        + self._getWordsRecur(num % (1000 ** p)))

    def numberToWords(self, num: int) -> str:
        """
        Use < 20, 10s, 1000^p to get words recursively.

        Time complexity: O(1).
        Space complexity: O(1).
        """
        if not num:
            return 'Zero'

        self.lessThan20 = ['One', 'Two', 'Three', 'Four', 'Five', 
                           'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                           'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                           'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        self.tens = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty',
                     'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.powersOfThousand = ['Thousand', 'Million', 'Billion']

        words = self._getWordsRecur(num)
        return ' '.join(words)


def main():
    # Output: "One Hundred Twenty Three"
    num = 123
    print(SolutionLessThan20TensPowersOfThousandsRecur().numberToWords(num))

    # Output: "Twelve Thousand Three Hundred Forty Five"
    num = 12345
    print(SolutionLessThan20TensPowersOfThousandsRecur().numberToWords(num))

    # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    num = 1234567
    print(SolutionLessThan20TensPowersOfThousandsRecur().numberToWords(num))

    # Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven 
    #          Thousand Eight Hundred Ninety One"
    num = 1234567891
    print(SolutionLessThan20TensPowersOfThousandsRecur().numberToWords(num))


if __name__ == '__main__':
    main()
