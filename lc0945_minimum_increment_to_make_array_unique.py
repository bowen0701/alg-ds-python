"""Leetcode 945. Minimum Increment to Make Array Unique
Medium

URL: https://leetcode.com/problems/minimum-increment-to-make-array-unique/

Given an array of integers A, a move consists of choosing any A[i], and
incrementing it by 1.

Return the least number of moves to make every value in A unique.

Example 1:
Input: [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
Input: [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to
have all unique values.

Note:
- 0 <= A.length <= 40000
- 0 <= A[i] < 40000
"""

class SolutionSortPrevPlusOne(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int

        Time complexity: O(n*logn), where n is A's length.
        Space complexity: O(1).
        """
        if not A:
            return 0

        # Sort the input array, compare current number with previous one.
        moves = need = 0
        for num in sorted(A):
            # Current number need to be at least previous + 1.
            moves += max(need - num, 0)
            need = max(num, need) + 1

        return moves


def main():
    # Output: 1
    A = [1, 2, 2]
    print SolutionSortPrevPlusOne().minIncrementForUnique(A)

    # Output: 6
    A = [3, 2, 1, 2, 1, 7]
        [1, 1, 2, 2, 3, 7]
    print SolutionSortPrevPlusOne().minIncrementForUnique(A)


if __name__ == '__main__':
    main()
