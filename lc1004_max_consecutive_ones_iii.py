"""Leetcode 1004. Max Consecutive Ones III
Medium

URL: https://leetcode.com/problems/max-consecutive-ones-iii/

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:
- 1 <= A.length <= 20000
- 0 <= K <= A.length
- A[i] is 0 or 1 
"""


class SolutionSlidingWindowMaxKZerosSubarray(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Translate problem into finding longest subarray w/ at most K zero.
        # Apply sliding window with two pointers to update max_len.
        max_len = 0
        n_zerios = 0
        i = 0

        # Iterate through A with right pointer j.
        for j in range(len(A)):
            # If A[j] is 0, increment n_zeros.
            if A[j] == 0:
                n_zerios += 1

            # If n_zerios overflows, move left i and decrement it if A[i] is 0.
            while n_zerios > K:
                if A[i] == 0:
                    n_zerios -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len


def main():
    # Output: 6
    A = [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
    print SolutionSlidingWindowMaxKZerosSubarray().longestOnes(A, K)

    # Output: 10
    A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    K = 3
    print SolutionSlidingWindowMaxKZerosSubarray().longestOnes(A, K)


if __name__ == '__main__':
    main()
