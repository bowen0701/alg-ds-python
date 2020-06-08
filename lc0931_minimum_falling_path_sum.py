"""Leetcode 931. Minimum Falling Path Sum
Medium

URL: https://leetcode.com/problems/minimum-falling-path-sum/

Given a square array of integers A, we want the minimum sum of a falling
path through A.

A falling path starts at any element in the first row, and chooses one
element from each row. The next row's choice must be in a column that is
different from the previous row's column by at most one.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation: 
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.
"""

class SolutionRecur(object):
    def _fallingPathSumRecur(self, A, r, c):
        # If at the 1st row, return its value.
        if r == 0:
            return A[r][c]

        n = len(A)
        min_sum = (A[r][c]
                   + min(self._fallingPathSumRecur(A, r - 1, max(0, c - 1)),
                         self._fallingPathSumRecur(A, r - 1, c),
                         self._fallingPathSumRecur(A, r - 1, min(n - 1, c + 1))))
        return min_sum

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int

        Time complexity: O(n*3^n), where n is the number of rows of A.
        Space complexity: O(n^2).
        """
        # Apply top-down recursion starting from the last row.
        # Edge case.
        if not A or not A[0]:
            return 0

        n = len(A)

        # Iterate through the last row to update min sum.
        min_sum = float('inf')
        for c in range(n):
            min_sum = min(min_sum, self._fallingPathSumRecur(A, n - 1, c))
        return min_sum


class SolutionMemo(object):
    def _fallingPathSumRecur(self, A, r, c, T):
        # Base case: if at the 1st row, return its value.
        if r == 0:
            return A[r][c]

        # Check memo table.
        if T[r][c]:
            return T[r][c]

        n = len(A)
        T[r][c] = (A[r][c]
                   + min(self._fallingPathSumRecur(A, r - 1, max(0, c - 1), T),
                         self._fallingPathSumRecur(A, r - 1, c, T),
                         self._fallingPathSumRecur(A, r - 1, min(n - 1, c + 1), T)))
        return T[r][c]

    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int

        Time complexity: O(n^2), where n is the number of rows of A.
        Space complexity: O(n^2).
        """
        # Apply top-down recursion with memoization, starting from the last row.
        # Edge case.
        if not A or not A[0]:
            return 0

        n = len(A)

        # Use a table T for memorizing the intermediate results.
        T = [[0] * n for _ in range(n)]

        # Iterate through the last row to update min sum.
        min_sum = float('inf')
        for c in range(n):
            min_sum = min(min_sum, self._fallingPathSumRecur(A, n - 1, c, T))
        return min_sum


class SolutionDP(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int

        Time complexity: O(n^2), where n is the number of rows of A.
        Space complexity: O(n^2).
        """
        # Apply bottom-up DP, starting from the 1st row.
        # Edge case.
        if not A or not A[0]:
            return 0

        n = len(A)

        # Use a table T for memorizing the intermediate results.
        T = [[float('inf')] * n for _ in range(n)]

        # Initialize the 1st row.
        for j in range(n):
            T[0][j] = A[0][j]

        for i in range(1, n):
            for j in range(n):
                T[i][j] = (A[i][j] 
                           + min(T[i - 1][max(0, j - 1)], 
                                 T[i - 1][j], 
                                 T[i - 1][min(n - 1, j + 1)]))
        return min(T[-1])


class SolutionDPOptim(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int

        Time complexity: O(n^2), where n is the number of rows of A.
        Space complexity: O(1).
        """
        # Apply bottom-up DP, starting from the 1st row.
        # Edge case.
        if not A or not A[0]:
            return 0

        n = len(A)

        for i in range(1, n):
            for j in range(n):
                A[i][j] += min(A[i - 1][max(0, j - 1)], 
                               A[i - 1][j], 
                               A[i - 1][min(n - 1, j + 1)])
        return min(A[-1])


def main():
    import time

    # Output: 12
    A = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    start_time = time.time()
    print 'Recur: {}'.format(SolutionRecur().minFallingPathSum(A))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Memo: {}'.format(SolutionMemo().minFallingPathSum(A))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'DP: {}'.format(SolutionDP().minFallingPathSum(A))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'DP optim: {}'.format(SolutionDPOptim().minFallingPathSum(A))
    print 'Time: {}'.format(time.time() - start_time)

    # Output: -66
    A = [[-80,-13,22],
         [ 83, 94,-5],
         [ 73,-48,61]]

    start_time = time.time()
    print 'Recur: {}'.format(SolutionRecur().minFallingPathSum(A))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'Memo: {}'.format(SolutionMemo().minFallingPathSum(A))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'DP: {}'.format(SolutionDP().minFallingPathSum(A))
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print 'DP optim: {}'.format(SolutionDPOptim().minFallingPathSum(A))
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
