"""Leetcode 461. Hamming Distance
Medium

URL: https://leetcode.com/problems/hamming-distance/description/

The Hamming distance between two integers is the number of positions at which 
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 <= x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       v   v

The above arrows point to positions where the corresponding bits 
are different.
"""

class SolutionBinCount(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(1).
        """
        return bin(x ^ y).count('1')


class SolutionModeTwoIter(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(1).
        """
        result = 0

        while x > 0 or y > 0:
            result += (x % 2) ^ (y % 2)
            x >>= 1
            y >>= 1

        return result


def main():
    print SolutionBinCount().hammingDistance(1, 4)
    print SolutionModeTwoIter().hammingDistance(1, 4)


if __name__ == '__main__':
    main()
