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

class SolutionEndGreedy(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        end = 0
        jumps = 0
        for i in range(n):
            print 'i:', i
            if end >= n:
                break

            if i + nums[i] > end:
                jumps += 1
                end = i + nums[i]
                print 'jumps:', jumps
                print 'end:', end

        return jumps


def main():
    # Outpout: 2
    nums = [2, 3, 1, 1, 4]
    print SolutionEndGreedy().jump(nums)


if __name__ == '__main__':
    main()
