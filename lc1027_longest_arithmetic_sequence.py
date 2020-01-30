"""Leetcode 1027. Longest Arithmetic Sequence
Medium

URL: https://leetcode.com/problems/longest-arithmetic-sequence/

Given an array A of integers, return the length of the longest arithmetic
subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with
0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic
if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

Example 1:
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].

Example 3:
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].

Note:
- 2 <= A.length <= 2000
- 0 <= A[i] <= 10000
"""

class SolutionPosDiffLenDp(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int

        Time complexity: O(n^2).
        Space complexity: O(n^2).
        """
        # Use dict:pos+diff->len to memorize previous pos's diff length.
        posdiff_len_d = {}

        n = len(A)

        for i in range(n):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                if (i, diff) not in posdiff_len_d:
                    # Initialize pos diff's count = 1+1.
                    posdiff_len_d[(j, diff)] = 2
                else:
                    posdiff_len_d[(j, diff)] = posdiff_len_d[(i, diff)] + 1

        return max(posdiff_len_d.values())


def main():
    # Output: 4
    A = [3,6,9,12]
    print SolutionPosDiffCountDp().longestArithSeqLength(A)

    # Output: 3
    A = [9,4,7,2,10]
    print SolutionPosDiffCountDp().longestArithSeqLength(A)

    # Output: 4
    A = [20,1,15,3,10,5,8]
    print SolutionPosDiffCountDp().longestArithSeqLength(A)


if __name__ == '__main__':
    main()
