"""Leetcode 832. Flipping an Image
Easy

URL: https://leetcode.com/problems/flipping-an-image/

Given a binary matrix A, we want to flip the image horizontally, then invert it,
and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:
Input: [[1,1,0],
        [1,0,1],
        [0,0,0]]
Output: [[1,0,0],
         [0,1,0],
         [1,1,1]]
Explanation: First reverse each row: 
[[0,1,1],
 [1,0,1],
 [0,0,0]].
Then, invert the image:
[[1,0,0],
 [0,1,0],
 [1,1,1]]

Example 2:
Input: [[1,1,0,0],
        [1,0,0,1],
        [0,1,1,1],
        [1,0,1,0]]
Output: [[1,1,0,0],
         [0,1,1,0],
         [0,0,0,1],
         [1,0,1,0]]
Explanation: First reverse each row:
[[0,0,1,1],
 [1,0,0,1],
 [1,1,1,0],
 [0,1,0,1]].
Then invert the image:
[[1,1,0,0],
 [0,1,1,0],
 [0,0,0,1],
 [1,0,1,0]]

Notes:
- 1 <= A.length = A[0].length <= 20
- 0 <= A[i][j] <= 1
"""

from typing import List


class Solution(object):
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        """
        Time complexity: O(rc), where r, c is the number of rows, cols, respectively
        Space complexity: O(1). 
        """
        # Iterate through each row.
        for r in range(len(A)):
            # Flip the image horizontally.
            j, k = 0, len(A[r]) - 1
            while j < k:
                A[r][j], A[r][k] = A[r][k], A[r][j]
                j += 1
                k -= 1

            # Invert the value.
            for c in range(len(A[r])):
                A[r][c] = 1 ^ A[r][c]

        return A


def main():
    # Output: [[1,0,0],[0,1,0],[1,1,1]]
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print Solution().flipAndInvertImage(A)

    # Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print Solution().flipAndInvertImage(A)


if __name__ == '__main__':
    main()
