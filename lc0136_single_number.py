"""Leetcode 136. Single Number
Easy

Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:
- Your algorithm should have a linear runtime complexity. 
- Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

class SolutionDict(object):
    def singleNumber(self, nums):
        """Lonely integer by naive dictionary.
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        num_count_d = {}
    
        for n in nums:
            if n in num_count_d:
                num_count_d[n] += 1
            else:
                num_count_d[n] = 1

        for num, count in num_count_d.items():
            if count == 1:
                return num


class SolutionBit(object):
    def singleNumber(self, nums):
        """Lonely integer by bit operation.
        :type nums: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        num = nums[0]
        for i, n in enumerate(nums, start=1):
            num ^= n
        return num


def main():
    import time

    # nums = [9, 1, 2, 3, 2, 9, 1, 7, 7]    # Single number = 3.
    # nums = [1, 3, 1, -1, 3]               # Single number = -1.
    nums = range(1000) + range(1000) + [1000]

    start_time = time.time()
    print('By extra dictionary: {}'
          .format(SolutionDict().singleNumber(nums)))
    print('Time: {}'.format(time.time() - start_time))

    start_time = time.time()
    print('By bit operation: {}'
          .format(SolutionBit().singleNumber(nums)))
    print('Time: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
