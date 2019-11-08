"""Leetcode 179. Largest Number
Medium

URL: https://leetcode.com/problems/largest-number/

Given a list of non negative integers, arrange them such that they form the
largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of
an integer.
"""

class SolutionSortComparator(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str

        Time complexity: O(m*n*logn), where 
          - n is the length of numbers
          - m is the max length of numbers
        Space complexity: O(m+n)
        """
        # Check any of numbers is larger than 0.
        if not any(nums):
            return '0'

        # Convert number list to string list.
        num_strs = [str(n) for n in nums]

        # Sort string list by built-in sort with comparator.
        def comparator(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        num_strs.sort(cmp=comparator)

        return ''.join(num_strs)


class SolutionSortComparator(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str

        Time complexity: O(m*n*logn), where 
          - n is the length of numbers
          - m is the max length of numbers
        Space complexity: O(m+n)
        """
        # Check any of numbers is larger than 0.
        if not any(nums):
            return '0'

        # Convert number list to string list.
        num_strs = [str(n) for n in nums]

        # Sort string list by built-in sort with comparator.
        def comparator(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0

        num_strs.sort(cmp=comparator)

        return ''.join(num_strs)


def main():
    # Output: "210"
    nums = [10,2]
    print SolutionSortComparator().largestNumber(nums)

    # Output: "9534330"
    nums = [3,30,34,5,9]
    print SolutionSortComparator().largestNumber(nums)

    nums = [0,0]
    print SolutionSortComparator().largestNumber(nums)    


if __name__ == '__main__':
    main()
