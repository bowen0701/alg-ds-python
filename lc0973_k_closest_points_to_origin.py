"""Leetcode 973. K Closest Points to Origin
Medium

URL: https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the
origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 
Note:
- 1 <= K <= points.length <= 10000
- -10000 < points[i][0] < 10000
- -10000 < points[i][1] < 10000
"""

from typing import List


class SolutionMaxHeap(object):
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time complexity: O(n*logk).
        Space complexity: O(k).
        """
        import heapq

        # Use maxheap with "negative" distance since heapq is min heap.
        negdistance_point_maxhq = []

        negdistances = [-(p[0] ** 2 + p[1] ** 2) for p in points]
        negdistances_points = zip(negdistances, points)

        for (nd, pt) in negdistances_points:
            heapq.heappush(negdistance_point_maxhq, (nd, pt))

            # Keep K points in maxheap.
            if len(negdistance_point_maxhq) > k:
                heapq.heappop(negdistance_point_maxhq)

        k_points = [pt for (nd, pt) in negdistance_point_maxhq]
        return k_points


class SolutionSelection(object):
    def _select(self, distances: List[int], k: int) -> int:
        # Select smaller & larger distance by pivot distanceance.
        n = len(distances)
        pivot_distance = distances[n // 2]

        small_distance = [d for d in distances if d < pivot_distance]
        mid_distance = [d for d in distances if d == pivot_distance]
        large_distance = [d for d in distances if d > pivot_distance]

        n_smalls = len(small_distance)
        n_mids = len(mid_distance)

        if k <= n_smalls:
            return self._select(small_distance, k)
        elif n_smalls < k <= n_smalls + n_mids:
            return pivot_distance
        else:
            return self._select(large_distance, k - n_smaller - n_mids)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        distances = [p[0] ** 2 + p[1] ** 2 for p in points]
        k_distance = self._select(distances, k)

        k_points = []
        for (d, p) in zip(distances, points):
            if d <= k_distance:
                # For fast list append.
                k_points += p,
        
        return k_points


def main():
    import time

    # Output: [[-2,2]]
    points = [[1,3],[-2,2]]
    k = 1

    start_time = time.time()
    print(SolutionMaxHeap().kClosest(points, k))
    print('MaxHeap: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(SolutionSelection().kClosest(points, k))
    print('Selection: {}'.format(time.time() - start_time))

    # Output: [[3,3],[-2,4]]
    points = [[3,3],[5,-1],[-2,4]]
    k = 2

    start_time = time.time()
    print(SolutionMaxHeap().kClosest(points, k))
    print('MaxHeap: {}'.format(time.time() - start_time))

    start_time = time.time()
    print(SolutionSelection().kClosest(points, k))
    print('Selection: {}'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
