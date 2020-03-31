"""Leetcode 1394. Find Lucky Integer in an Array
Easy

URL: https://leetcode.com/problems/find-lucky-integer-in-an-array/

Given an array of integers arr, a lucky integer is an integer which has a
frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers
return the largest of them. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Example 4:
Input: arr = [5]
Output: -1

Example 5:
Input: arr = [7,7,7,7,7,7,7]
Output: 7
 
Constraints:
- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500
"""


class SolutionDict(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Create a dict:num->freq.
        num_freq_d = defaultdict(int)
        for num in arr:
            num_freq_d[num] += 1

        # Iterate through dict keys to collect lucky nums.
        lucky_nums = []
        for num, freq in num_freq_d.items():
            if num == freq:
                lucky_nums.append(num)

        # Return max lucky number if existed.
        if lucky_nums:
            return max(lucky_nums)
        else:
            return -1


def main():
    # Output: 2
    arr = [2,2,3,4]
    print SolutionDict().findLucky(arr)

    # Output: 3
    arr = [1,2,2,3,3,3]
    print SolutionDict().findLucky(arr)

    # Output: -1
    arr = [2,2,2,3,3]
    print SolutionDict().findLucky(arr)
    
    # Output: -1
    arr = [5]
    print SolutionDict().findLucky(arr)
    
    # Output: 7
    arr = [7,7,7,7,7,7,7]
    print SolutionDict().findLucky(arr)


if __name__ == '__main__':
    main()
