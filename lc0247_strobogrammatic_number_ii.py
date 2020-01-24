"""Leetcode 247. Strobogrammatic Number II
Medium

URL: https://leetcode.com/problems/strobogrammatic-number-ii/

A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:
Input:  n = 2
Output: ["11","69","88","96"]
"""

class SolutionInsertMiddleRecur(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]

        Observations:
        - n=0: ''
        - n=1: '0', '1', '8'
        - n=2: '11', '69', '88', '96'
        - n=3: Insert '0', '1', '8' into middle of Strobogrammatic(n=2)
        - n=4: Insert '00', '11', '69', '88', '96' into middel of Strobogrammatic(n=2)
        - n=5: Insert '0', '1', '8' into middel of Strobogrammatic(n=4)
        - n=6: Insert '00', '11', '69', '88', '96' into middel of Strobogrammatic(n=4)

        Time complexity: O(5^(n/2)).
        Space complexity: O(n).      
        """
        # Edge cases.
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '8']
        if n == 2:
            return ['11', '69', '88', '96']

        odd_mid_strs = ['0', '1', '8']
        even_mid_strs = ['00', '11', '69', '88', '96']

        if n % 2 == 1:
            mid_strs = odd_mid_strs
            outer_strs = self.findStrobogrammatic(n - 1)
        else:
            mid_strs = even_mid_strs
            outer_strs = self.findStrobogrammatic(n - 2)

        # Insert middle string into middle pos of outer string.
        mid = (n - 1) // 2
        result = []
        for outer_str in outer_strs:
            for mid_str in mid_strs:
                result.append(outer_str[:mid] + mid_str + outer_str[mid:])

        return result


def main():
    n = 0
    print SolutionInsertMiddleRecur().findStrobogrammatic(n)

    n = 1
    print SolutionInsertMiddleRecur().findStrobogrammatic(n)

    n = 2
    print SolutionInsertMiddleRecur().findStrobogrammatic(n)

    n = 3
    print SolutionInsertMiddleRecur().findStrobogrammatic(n)

    n = 4
    print SolutionInsertMiddleRecur().findStrobogrammatic(n)


if __name__ == '__main__':
    main()
