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

class SolutionBruteForce(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int

        Note: Time limit exceeded.

        Time complexity: O(n^2), where n is A's length.
        Space complexity: O(n).
        """
        from collections import defaultdict

        if not A:
            return 0

        # Create a dict:number->count.
        num_count_d = defaultdict(int)
        for num in A:
            num_count_d[num] += 1

        # While exists repeated numbers, move number by incrementing it.
        moves = 0
        repeated_nums = set([num for num, count in num_count_d.items() 
                             if count > 1])
        while repeated_nums:
            num = repeated_nums.pop()
            while num_count_d[num] > 1:
                num_count_d[num] -= 1
                num_count_d[num + 1] += 1
                moves += 1

                # If num's or num + 1's counts > 1, add back to set.
                if num_count_d[num] > 1:
                    repeated_nums.add(num)
                if num_count_d[num + 1] > 1:
                    repeated_nums.add(num + 1)

        return moves


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
        print sorted(A)
        for num in sorted(A):
            # Current number need to be at least previous + 1.
            moves += max(need - num, 0)
            need = max(num, need) + 1

        return moves


def main():
    # Output: 1
    A = [1, 2, 2]
    print SolutionBruteForce().minIncrementForUnique(A)
    print SolutionSortPrevPlusOne().minIncrementForUnique(A)

    # Output: 6
    A = [3, 2, 1, 2, 1, 7]
    print SolutionBruteForce().minIncrementForUnique(A)
    print SolutionSortPrevPlusOne().minIncrementForUnique(A)


if __name__ == '__main__':
    main()
