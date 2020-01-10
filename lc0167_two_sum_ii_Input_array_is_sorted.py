"""Leetcode 167. Two Sum II - Input array is sorted
Easy

URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they
add up to the target, where index1 must be less than index2.

Note:
- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have exactly one solution and
  you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

class SolutionBinarySearch(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            two_sum = numbers[left] + numbers[right]

            if two_sum == target:
                return [left + 1, right + 1]
            elif two_sum < target:
                left += 1
            else:
                right -= 1


def main():
    # Output: [1, 2]
    numbers, target = [2,7,11,15], 9
    print SolutionBinarySearch().twoSum(numbers, target)


if __name__ == '__main__':
    main()
