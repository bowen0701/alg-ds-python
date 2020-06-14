"""Leetcode 55. Jump Game
Medium

URL: https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""

class SolutionGreedy(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Create max reachable index.
        reach = 0

        for i in range(len(nums)):
            # Check if index i is not reachable.
            if reach < i:
                return False

            # Update reach by taking max of itself and i+nums[i].
            reach = max(reach, i + nums[i])

        return True


def main():
    # Ans: True
    nums = [2,3,1,1,4]
    print SolutionGreedy().canJump(nums)

    # Ans: False
    nums = [3,2,1,0,4]
    print SolutionGreedy().canJump(nums)


if __name__ == '__main__':
    main()
