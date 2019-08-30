"""Leetcode 189. Rotate Array
Easy

URL: https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
- Try to come up as many solutions as you can, 
  there are at least 3 different ways to solve this problem.
- Could you do it in-place with O(1) extra space?
"""

class SolutionCopy(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # If k >= n, truncate k by n.
        n = len(nums)
        k = k % n

        # Append right with left.
        nums[:] = nums[-k:] + nums[:-k]


class SolutionIter(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # If k >= n, truncate k by n.
        n = len(nums)
        k = k % n

        count = 0
        start_pos, cur_pos = 0, 0

        while count < n:
            next_pos = (cur_pos + k) % n
            temp_num = nums[next_pos]
            # TODO: 2019/08/30
            nums[new] = rotate_num
            rotate_num = temp_num

            while current != start:


                count += 1
                print nums

            start += 1
            current = s

        nums[new_id] = old_num


def main():
    # Ans: [5,6,7,1,2,3,4]
    nums = [1,2,3,4,5,6,7]
    k = 3
    print nums
    # SolutionCopy().rotate(nums, k)
    SolutionIter().rotate(nums, k)
    print nums

    # Ans: [3,99,-1,-100]
    nums = [-1,-100,3,99]
    k = 2
    print nums
    # SolutionCopy().rotate(nums, k)
    SolutionIter().rotate(nums, k)
    print nums

    # Ans: [2,1]
    nums = [1,2]
    k = 3
    print nums
    # SolutionCopy().rotate(nums, k)
    SolutionIter().rotate(nums, k)
    print nums


if __name__ == '__main__':
    main()
