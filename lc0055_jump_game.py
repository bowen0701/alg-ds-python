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


class SolutionDP(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply bottom-up DP with memo table T, where T[i] = True means reachable.
        n = len(nums)
        T = [False] * n
        T[0] = True

        # Check if i is reachable from some reachable j.
        for i in range(1, n):
            for j in range(i, -1, -1):
                if i - j <= nums[j] and T[j]:
                    T[i] = True
                    break
        return T[-1]


class SolutionGreedy(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply greedy approach with early stopping.
        # Create max reachable index.
        reach = 0

        for i in range(len(nums)):
            # Check if ifndex i is not reachable.
            if reach < i:
                return False

            # Update reach by taking max of itself and i+nums[i].
            reach = max(reach, i + nums[i])

        return True


def main():
    import time

    # Ans: True
    nums = [2,3,1,1,4]

    start_time = time.time()
    print 'DP:', SolutionDP().canJump(nums)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'DP:', SolutionGreedy().canJump(nums)
    print 'Time:', time.time() - start_time

    # Ans: False
    nums = [3,2,1,0,4]

    start_time = time.time()
    print 'DP:', SolutionDP().canJump(nums)
    print 'Time:', time.time() - start_time

    start_time = time.time()
    print 'DP:', SolutionGreedy().canJump(nums)
    print 'Time:', time.time() - start_time


if __name__ == '__main__':
    main()
