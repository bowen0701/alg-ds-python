"""Leetcode 743. Network Delay Time
Medium

URL: https://leetcode.com/problems/network-delay-time/

You are given a network of n nodes, labeled from 1 to n. You are also given
times, a list of travel times as directed edges times[i] = (ui, vi, wi),
where ui is the source node, vi is the target node, and wi is the time it
takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes
for all the n nodes to receive the signal. If it is impossible for all the
n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

Constraints:
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

Core algorithm: Dijkstra's single-source shortest path.
See also: alg_dijkstra_shortest_path.py
"""

import heapq
from collections import defaultdict
from typing import List


class SolutionDijkstra:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Time complexity: O((|V|+|E|)log|V|).
        Space complexity: O(|V|+|E|).
        """
        # Build adjacency dict from edge list.
        graph = defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        # Dijkstra: single-source shortest path with min-heap.
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        min_heap = [(0, k)]

        while min_heap:
            d, u = heapq.heappop(min_heap)

            # Skip stale entries.
            if d > dist[u]:
                continue

            for v, w in graph[u].items():
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(min_heap, (dist[v], v))

        ans = max(dist.values())
        return ans if ans < float('inf') else -1


def main():
    # Output: 2
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n, k = 4, 2
    print(SolutionDijkstra().networkDelayTime(times, n, k))

    # Output: 1
    times = [[1, 2, 1]]
    n, k = 2, 1
    print(SolutionDijkstra().networkDelayTime(times, n, k))

    # Output: -1
    times = [[1, 2, 1]]
    n, k = 2, 2
    print(SolutionDijkstra().networkDelayTime(times, n, k))


if __name__ == '__main__':
    main()
