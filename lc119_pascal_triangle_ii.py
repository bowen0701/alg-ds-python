"""Leetcode 119. Pascal's Triangle II
Easy

URL: https://leetcode.com/problems/pascals-triangle-ii/

Given a non-negative index k where k <= 33, return the kth index row of the 
Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly 
above it.

Example:
Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]

        Time complexity: O(k^2).
        Space complexity: O(k).
        """
        if rowIndex <= 1:
            return [1] * (rowIndex + 1)

        last_row = [1] * 2
        for r in range(2, rowIndex + 1):
            row = [1] * (r + 1)
            for i in range(1, r):
                row[i] = last_row[i - 1] + last_row[i]
            last_row = row
        return row


def main():
    rowIndex = 3
    print 'kth row of the Pascal\'s triangle: {}'.format(
        Solution().getRow(rowIndex))


if __name__ == '__main__':
    main()
