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
        Space complexity: O(1).
        """
        # If k >= n, truncate k by n.
        n = len(nums)
        k = k % n

        # Start from the 0th.
        i = 0
        count = 0

        # Iterate through nums to rotate them until all is updated.
        while count < n:
            # Backup current, and update current by the ith.
            cur_pos = (i + k) % n
            cur_num = nums[cur_pos]
            nums[cur_pos] = nums[i]
            
            count += 1
            j = cur_pos

            # If no cycle, continue rotating current & next nums.
            while j != i and count < n:
                next_pos = (j + k) % n
                # Swap current and next nums; current num -> next num.
                cur_num, nums[next_pos] = nums[next_pos], cur_num

                count += 1
                j = next_pos

            # Increment start i.
            i += 1


def main():
    # Ans: [5,6,7,1,2,3,4]
    nums = [1,2,3,4,5,6,7]
    k = 3
    print 'Raw:', nums, 'k:', k
    # SolutionCopy().rotate(nums, k)
    SolutionIter().rotate(nums, k)
    print 'Rotated', nums

    # Ans: [3,99,-1,-100]
    nums = [-1,-100,3,99]
    k = 2
    print 'Raw:', nums, 'k:', k
    # SolutionCopy().rotate(nums, k)
    SolutionIter().rotate(nums, k)
    print 'Rotated', nums

    # Ans: [2,1]
    nums = [1,2]
    k = 3
    print 'Raw:', nums, 'k:', k
    # SolutionCopy().rotate(nums, k)
    SolutionIter().rotate(nums, k)
    print 'Rotated', nums


if __name__ == '__main__':
    main()
