"""Leetcode. Optimal Utilization

URL: https://leetcode.com/discuss/interview-question/373202

Given 2 lists a and b. Each element is a pair of integers where
the first integer represents the unique id and
the second integer represents a value.
Your task is to find an element from a and an element form b such that the
sum of their values is less or equal to target and as close to target as possible.
Return a list of ids of selected elements.
If no pair is possible, return an empty list.

Example 1:
Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7
Output: [[2, 1]]
Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1],
which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

Example 2:
Input:
a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
Output: [[2, 4], [3, 2]]
Explanation:
There are two pairs possible. Element with id = 2 from the list `a` has a value 5,
and element with id = 4 from the list `b` also has a value 5.
Combined, they add up to 10. Similarily, element with id = 3 from `a` has a value 7,
and element with id = 2 from `b` has a value 3.
These also add up to 10. Therefore, the optimal pairs are [2, 4] and [3, 2].
"""

class SolutionTwoPointers(object):
    def optimizeUtilization(self, max_dist, forwards, returns):
        """
        :type max_dist: Int
        :type forwards: List[Int, Int]
        :type returns: List[Int, Int] 
        :rtype: List[List[Int]]

        Time complexity: O(m*logm + n*logn + m + n) = O(max(m*logm, n*logn)), where
          - m is the number of forwards,
          - n is the number of returns.
        Space complexity: O(m*n), in "worst" case, all pairs contribute the result.
        """
        from collections import defaultdict

        if not forwards or not returns:
            return []

        n_forwards, n_returns = len(forwards), len(returns)
        
        # First sort two routes by value.
        forwards.sort(key=lambda x: x[1])
        returns.sort(key=lambda x: x[1])
        # a = [[1, 3], [2, 5], [3, 7], [4, 10]]
        # b = [[1, 2], [2, 3], [3, 4], [4, 5]]

        # Use a dict to store distance sums and the corresponding elements.
        sums_d = defaultdict(list)

        # Initialize a distance upper bound.
        upper_dist = -1

        # Apply two pointer method: 
        # - left: start from the start of forwards, end at its last.
        # - right: start from the end of returns, end at 0.
        left, right = 0, n_returns - 1

        while left < n_forwards and right >= 0:
            sum_dist = forwards[left][1] + returns[right][1]
            
            # If distance sum > max distance, decrement right.
            if sum_dist > max_dist:
                right -= 1
                continue

            # Iterate to get the pairs of max sum distance <= max distance.
            if sum_dist >= upper_dist:
                # Set temporary right: r.
                r = right

                # Iterate over returns with the same distance sum.
                while r >= 0 and returns[r] == returns[right]:
                    sums_d[sum_dist] += [[forwards[left][0], returns[r][0]]]
                    r -= 1

                # Update upper distance by distance sum.
                upper_dist = sum_dist

            # Increment left to see if there are more pairs satisfying max distance.
            left += 1

        return sums_d[upper_dist]


def main():
    # Output: [[2, 1]]
    forwards = [[1, 2], [2, 4], [3, 6]]
    returns = [[1, 2]]
    max_dist = 7
    print SolutionTwoPointers().optimizeUtilization(max_dist, forwards, returns)

    # Output: [[2, 4], [3, 2]]
    forwards = [[1, 3], [2, 5], [3, 7], [4, 10]]
    returns = [[1, 2], [2, 3], [3, 4], [4, 5]]
    max_dist = 10
    print SolutionTwoPointers().optimizeUtilization(max_dist, forwards, returns)


if __name__ == '__main__':
    main()
