"""Leetcode 787. Cheapest Flights Within K Stops
Medium

URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by some number of flights. You are given an
array flights where flights[i] = [fromi, toi, pricei] indicates that
there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest
price from src to dst with at most k stops. If there is no such route,
return -1.

Example 1:
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],
src = 0, dst = 3, k = 1
Output: 700
Explanation: The optimal path with at most 1 stop from city 0 to 3 is
0 -> 1 -> 3 with cost 100 + 600 = 700.

Example 2:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]],
src = 0, dst = 2, k = 1
Output: 200

Example 3:
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]],
src = 0, dst = 2, k = 0
Output: 500

Constraints:
- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 10^4
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst
"""

from typing import List


class SolutionBellmanFord:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        """
        Time complexity: O(k * |E|).
        Space complexity: O(n).
        """
        # Bellman-Ford: relax all edges k+1 times.
        min_cost = [float('inf')] * n
        min_cost[src] = 0

        for _ in range(k + 1):
            # Use a copy to avoid using updates from the same iteration.
            prev = min_cost[:]

            for u, v, w in flights:
                if prev[u] + w < min_cost[v]:
                    min_cost[v] = prev[u] + w

        return min_cost[dst] if min_cost[dst] != float('inf') else -1


class SolutionBFS:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        """
        Time complexity: O(n * k).
        Space complexity: O(n * k).
        """
        from collections import defaultdict, deque

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # BFS level by level, each level = one stop.
        queue = deque([(src, 0)])
        # min_cost[i]: min cost from src to node i seen so far, for pruning.
        min_cost = [float('inf')] * n
        min_cost[src] = 0
        stops = 0

        while queue and stops <= k:
            for _ in range(len(queue)):
                node, cost = queue.popleft()

                for neighbor, price in graph[node]:
                    new_cost = cost + price
                    if new_cost < min_cost[neighbor]:
                        min_cost[neighbor] = new_cost
                        queue.append((neighbor, new_cost))

            stops += 1

        return min_cost[dst] if min_cost[dst] != float('inf') else -1


class SolutionDijkstra:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int,
    ) -> int:
        """
        Time complexity: O(n * k * log(n * k)).
        Space complexity: O(n * k).
        """
        from collections import defaultdict
        import heapq

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # (cost, node, stops_left).
        heap = [(0, src, k + 1)]
        # Track best stops_left when visiting a node.
        best_stops_left = {}

        while heap:
            cost, node, stops_left = heapq.heappop(heap)

            if node == dst:
                return cost

            if node in best_stops_left and best_stops_left[node] >= stops_left:
                continue
            best_stops_left[node] = stops_left

            if stops_left > 0:
                for next_node, price in graph[node]:
                    heapq.heappush(heap, (cost + price, next_node, stops_left - 1))

        return -1


def main():
    # Output: 700.
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src, dst, k = 0, 3, 1
    print(SolutionBellmanFord().findCheapestPrice(n, flights, src, dst, k))
    print(SolutionBFS().findCheapestPrice(n, flights, src, dst, k))
    print(SolutionDijkstra().findCheapestPrice(n, flights, src, dst, k))

    # Output: 200.
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src, dst, k = 0, 2, 1
    print(SolutionBellmanFord().findCheapestPrice(n, flights, src, dst, k))
    print(SolutionBFS().findCheapestPrice(n, flights, src, dst, k))
    print(SolutionDijkstra().findCheapestPrice(n, flights, src, dst, k))

    # Output: 500.
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src, dst, k = 0, 2, 0
    print(SolutionBellmanFord().findCheapestPrice(n, flights, src, dst, k))
    print(SolutionBFS().findCheapestPrice(n, flights, src, dst, k))
    print(SolutionDijkstra().findCheapestPrice(n, flights, src, dst, k))


if __name__ == '__main__':
    main()
