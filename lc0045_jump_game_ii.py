"""Leetcode 45. Jump Game II
Hard

URL: https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers, you are initially positioned at
the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
"""

class SolutionPrevEndAndEndGreedy(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n), where n is length of nums.
        Space complexity: O(1).
        """
        n = len(nums)

        # Apply greedy algorithm to check index i in prev_end and end.
        prev_end, end = -1, 0
        jumps = 0

        for i in range(n):
            # Check if reached last index already.
            if end >= n - 1:
                break

            # Update jump if current index is behind prev_end.
            if prev_end < i:
                jumps += 1
                prev_end = end

            # Update end with current index and jump.
            end = max(end, i + nums[i])

        return jumps


def main():
    # Outpout: 2
    nums = [2,3,1,1,4]
    print SolutionPrevEndAndEndGreedy().jump(nums)

    # Outpout: 2
    nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    print SolutionPrevEndAndEndGreedy().jump(nums)


if __name__ == '__main__':
    main()
