"""Leetcode 905. Sort Array By Parity
Easy

URL: https://leetcode.com/problems/sort-array-by-parity/

Given an array A of non-negative integers, return an array consisting of all the
even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
- 1 <= A.length <= 5000
- 0 <= A[i] <= 5000
"""

class SolutionTwoArrays(object):
    def sortArrayByParity(self, A):
        """
        Collect even and odd numbers in two arrays, and then concat them.

        :type A: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(n).
        """
        evens, odds = [], []

        for n in A:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)

        evens.extend(odds)
        return evens


class SolutionEvenPointer(object):
    def sortArrayByParity(self, A):
        """
        Use even index to switch even and odd numbers.

        :type A: List[int]
        :rtype: List[int]

        Time complexity: O(n).
        Space complexity: O(1).
        """
        even_idx = 0

        for i, n in enumerate(A):
            if n % 2 == 0:
                # Swap number i and even index, and increment even index.
                A[even_idx], A[i] = A[i], A[even_idx]
                even_idx += 1

        return A


def main():
    # Output:  [2,4,3,1]
    A =  [3,1,2,4]
    print SolutionTwoArrays().sortArrayByParity(A)
    print SolutionEvenPointer().sortArrayByParity(A)


if __name__ == '__main__':
    main()
