"""Leetcode 1395. Count Number of Teams
Medium

URL: https://leetcode.com/problems/count-number-of-teams/

There are n soldiers standing in a line. Each soldier is assigned a unique
rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] >
rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions.
(soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions.
(2,3,4), (5,4,1), (5,3,1).

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4
 
Constraints:
- n == rating.length
- 1 <= n <= 200
- 1 <= rating[i] <= 10^5
"""

class SolutionBruteForce(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int

        Time complexity: O(n^3).
        Space complexity: O(1).
        """
        n = len(rating)
        
        # Edge case.
        if n <= 2:
            return 0

        result = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if (rating[i] - rating[j]) * (rating[j] - rating[k]) > 0:
                        result += 1

        return result


class SolutionLeftRightGreaterLess(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int

        Time complexity: O(n^2).
        Space complexity: O(1).
        """
        n = len(rating)

        # Edge case.
        if n <= 2:
            return 0

        # Iterate through rating to find increasing/decreasing rating.
        result = 0
        for i in range(n):
            # Get left/right's greater/less for each element i.
            left_less = right_greater = 0
            left_greater = right_less = 0

            for j in range(n):
                if i < j:
                    if rating[i] < rating[j]:
                        right_greater += 1
                    else:
                        right_less += 1
                elif j < i:
                    if rating[j] < rating[i]:
                        left_less += 1
                    else:
                        left_greater += 1

            result += left_less * right_greater + left_greater * right_less

        return result


def main():
    import time

    # Output: 3
    rating = [2,5,3,4,1]

    start_time = time.time()
    print SolutionBruteForce().numTeams(rating)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionLeftRightGreaterLess().numTeams(rating)
    print 'Time: {}'.format(time.time() - start_time)

    # Output: 0
    rating = [2,1,3]

    start_time = time.time()
    print SolutionBruteForce().numTeams(rating)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionLeftRightGreaterLess().numTeams(rating)
    print 'Time: {}'.format(time.time() - start_time)

    # Output: 4
    rating = [1,2,3,4]

    start_time = time.time()
    print SolutionBruteForce().numTeams(rating)
    print 'Time: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionLeftRightGreaterLess().numTeams(rating)
    print 'Time: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
