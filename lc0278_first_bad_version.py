"""Leetcode 278. First Bad Version
Easy

URL: https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a 
new product. Unfortunately, the latest version of your product fails 
the quality check. Since each version is developed based on the previous 
version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the 
first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether 
version is bad. Implement a function to find the first bad version. 
You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return VERSION_FAILURES[version - 1]


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        start = 1
        final = n

        while final - start > 0:
            middle = start + (final - start) // 2
            if isBadVersion(middle):
                # Since middle is bad, use it as next final.
                final = middle
            else:
                # Since middle is good, use its next as next start.
                start = middle + 1

        return final


def main():
    global VERSION_FAILURES
    VERSION_FAILURES = [False] * 1000 + [True] * 100
    n = len(VERSION_FAILURES)
    
    print Solution().firstBadVersion(n)


if __name__ == '__main__':
    main()
