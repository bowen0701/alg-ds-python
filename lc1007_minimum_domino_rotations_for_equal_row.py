"""Leetcode 1007. Minimum Domino Rotations For Equal Row
Medium

URL: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the 
i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half
of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same,
or all the values in B are the same.

If it cannot be done, return -1.

Example 1:
Input: A = [2,1,2,4,2,2], 
       B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any
rotations.
If we rotate the second and fourth dominoes, we can make every value in the top
row equal to 2, as indicated by the second figure.

Example 2:
Input: A = [3,5,1,2,3], 
       B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

Note:
- 1 <= A[i], B[i] <= 6
- 2 <= A.length == B.length <= 20000
"""

class SolutionNumCounts(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        n = len(A)

        # Create 1~6 number counts for A and B and at the same pos if A[i] == B[i]. 
        A_num_counts = [0] * 7
        B_num_counts = [0] * 7
        same_num_counts = [0] * 7

        for i in range(n):
            A_num_counts[A[i]] += 1
            B_num_counts[B[i]] += 1

            if A[i] == B[i]:
                same_num_counts[A[i]] += 1

        # Check iteratively all in numbers, their union set cover the whole list.
        for j in range(1, 7):
            if A_num_counts[j] + B_num_counts[j] - same_num_counts[j] == n:
                return min(n - A_num_counts[j], n - B_num_counts[j])

        return -1
        

def main():
    # Output: 2
    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]
    print SolutionNumCounts().minDominoRotations(A, B)

    # Output: -1
    A = [3,5,1,2,3]
    B = [3,6,3,3,4]
    print SolutionNumCounts().minDominoRotations(A, B)

    # Output: 2
    A = [1,5,1,2,3]
    B = [3,3,3,3,4]
    print SolutionNumCounts().minDominoRotations(A, B)


if __name__ == '__main__':
    main()
