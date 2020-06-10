"""Leetcode 896. Monotonic Array
Easy

URL: https://leetcode.com/problems/monotonic-array/

An array is monotonic if it is either monotone increasing or monotone decreasing.
- An array A is monotone increasing if for all i <= j, A[i] <= A[j].
- An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true

Example 3:
Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true

Note:
- 1 <= A.length <= 50000
- -100000 <= A[i] <= 100000
"""

class SolutionTwoBooleans(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(2).
        """
        is_increasing = True
        is_decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                is_increasing = False
            
            if A[i] < A[i + 1]:
                is_decreasing = False

            # Enable early stopping.
            if not is_increasing and not is_decreasing:
                return False

        return True


def main():
    # Output: True
    A = [1,2,2,3]
    print SolutionTwoBooleans().isMonotonic(A)

    # Output: True
    A = [6,5,4,4]
    print SolutionTwoBooleans().isMonotonic(A)

    # Output: False
    A = [1,3,2]
    print SolutionTwoBooleans().isMonotonic(A)

    # Output: True
    A = [1,2,4,5]
    print SolutionTwoBooleans().isMonotonic(A)

    # Output: True
    A = [1,1,1]
    print SolutionTwoBooleans().isMonotonic(A)


if __name__ == '__main__':
    main()
