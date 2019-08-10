"""Leetcode 69. Sqrt(x)
Easy

URL: https://leetcode.com/problems/sqrtx/

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a 
non-negative integer.

Since the return type is an integer, the decimal digits are truncated and 
only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        Time complexity: O(logx).
        Space complexity: O(1).
        """
        if not x:
        	return 0

        # Apply binary search with last = x // 2 for smaller search space.
        first = 1
        last = x // 2

        while first < last:
        	mid = first + (last - first) // 2
        	mid_squared = mid ** 2

        	if mid_squared == x:
        		return mid
        	elif mid_squared > x:
        		last = mid - 1
        	else:
        		first = mid + 1
        
        # Final check for first: if too big, minus 1.
        if first ** 2 > x:
        	return first - 1

        return first


def main():
	x = 4
	print Solution().mySqrt(x)

	x = 8
	print Solution().mySqrt(x)

	x = 100
	print Solution().mySqrt(x)

	x = 102
	print Solution().mySqrt(x)


if __name__ == '__main__':
	main()
