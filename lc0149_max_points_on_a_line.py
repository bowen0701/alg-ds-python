"""Leetcode 149. Max Points on a Line
Hard

URL: https://leetcode.com/problems/max-points-on-a-line/

Given n points on a 2D plane, find the maximum number of points that
lie on the same straight line.

Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

NOTE: input types have been changed on April 15, 2019.
Please reset to default code definition to get new method signature.
"""

class Solution(object):
    def _gcd(self, a, b):
        """Greatest common divisor."""
        if b == 0:
            return a
        return self._gcd(b, a % b)

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        n = len(points)
        if n <= 2:
            return n

        # Compute lines based on point pairs, add to dict: (intercept, slope)->points.
        interceptslope_point_d = defaultdict(list)

        for i in range(n - 1):
            for j in range(i + 1, n):
                p1 = points[i]
                p2 = points[j]
                # TODO



def main():
    pass


if __name__ == '__main__':
    main()
