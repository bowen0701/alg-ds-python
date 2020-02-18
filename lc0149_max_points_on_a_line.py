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
    def _gcd(self, x, y):
        """Greatest common divisor."""
        if y == 0:
            return x
        return self._gcd(y, x % y)

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        n = len(points)
        if n <= 2:
            return n

        # Use dict: line's (a, b, c)->points, where line is ax+by+c=0.
        line_points_d = defaultdict(list)

        for i in range(n - 1):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2:
                    # line: x = x1
                    a, b, c = 1, 0, -x1
                else:
                    # TODO


def main():
    pass


if __name__ == '__main__':
    main()
