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


class SolutionGreaterLess(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int

        Time complexity: O(n^2).
        Space complexity: O(n).
        """
        n = len(rating)

        # Edge case.
        if n <= 2:
            return 0

        # Use greaters & lesses to get counters > or < than rating[i].
        greaters = [0] * n
        lesses = [0] * n

        # Iterate through rating to find increasing rating.

        # Iterate through rating to find decreasing rating.


def main():
    # Output: 3
    rating = [2,5,3,4,1]
    print SolutionBruteForce().numTeams(rating)

    # Output: 0
    rating = [2,1,3]
    print SolutionBruteForce().numTeams(rating)

    # Output: 4
    rating = [1,2,3,4]
    print SolutionBruteForce().numTeams(rating)


if __name__ == '__main__':
    main()
