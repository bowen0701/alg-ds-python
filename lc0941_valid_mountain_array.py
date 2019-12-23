"""Leetcode 941. Valid Mountain Array
Easy

URL: https://leetcode.com/problems/valid-mountain-array/

Given an array A of integers, return true if and only if it is a valid
mountain array.

Recall that A is a mountain array if and only if:
- A.length >= 3
- There exists some i with 0 < i < A.length - 1 such that:
  * A[0] < A[1] < ... A[i-1] < A[i]
  * A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note:
- 0 <= A.length <= 10000
- 0 <= A[i] <= 10000 
"""

class SolutionIter(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Edge case.
        if len(A) <= 2:
            return False

        # Start from pos 0 to iteratively check strictly increasing.
        i = 0
        while i < len(A) and i + 1 < len(A) and A[i] < A[i + 1]:
            i += 1

        # If not strictly increasing at beginning or at all.
        if i == 0 or i == len(A) - 1:
            return False

        # Start from last pos to check strictly decreasing.
        while i < len(A) and i + 1 < len(A):
            if A[i] <= A[i + 1]:
                return False
            i += 1

        return True


def main():
    # Output: false
    A = [2,1]
    print SolutionIter().validMountainArray(A)

    # Output: false
    A = [3,5,5]
    print SolutionIter().validMountainArray(A)

    # Output: true
    A = [0,3,2,1]
    print SolutionIter().validMountainArray(A)


if __name__ == '__main__':
    main()
