"""Leetcode 1167 Minimum Cost to Connect Sticks
Medium
(Premium)

URL: https://leetcode.com/problems/minimum-cost-to-connect-sticks

Given n ropes of different lengths, we need to connect these ropes into one rope.
We can connect only 2 ropes at a time.
The cost required to connect 2 ropes is equal to sum of their lengths.
The length of this connected rope is also equal to the sum of their lengths.
This process is repeated until n ropes are connected into a single rope.
Find the min possible cost required to connect all ropes.

Example 1:
Input: ropes = [8, 4, 6, 12]
Output: 58
Explanation: The optimal way to connect ropes is as follows
1. Connect the ropes of length 4 and 6 (cost is 10).
   Ropes after connecting: [8, 10, 12]
2. Connect the ropes of length 8 and 10 (cost is 18).
   Ropes after connecting: [18, 12]
3. Connect the ropes of length 18 and 12 (cost is 30).
Total cost to connect the ropes is 10 + 18 + 30 = 58

Example 2:
Input: ropes = [20, 4, 8, 2]
Output: 54

Example 3:
Input: ropes = [1, 2, 5, 10, 35, 89]
Output: 224

Example 4:
Input: ropes = [2, 2, 3, 3]
Output: 20
"""

class SolutionMinHeap(object):
    def minCost(self, ropes):
        """
        :type self: List[int]
        :rtype: int

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        # Every time add the two shortest ropes by min heap.
        import heapq

        if not ropes:
            return 0

        if len(ropes) <= 2:
            return sum(ropes)

        min_cost = 0

        min_h = ropes
        heapq.heapify(min_h)

        while len(min_h) > 1:
            # Add the first 2 shortest ropes for additional cost.
            min_rope1 = heapq.heappop(min_h)
            
            if min_h:
                min_rope2 = heapq.heappop(min_h)
            else:
                min_repe2 = 0
            
            add_cost = min_rope1 + min_rope2

            # Accumulate min cost with additional cost.
            min_cost += add_cost

            # Push the additional cost to min heap.
            heapq.heappush(min_h, add_cost)

        return min_cost


def main():
    # Ans: 58
    ropes = [8, 4, 6, 12]
    print Solution().minCost(ropes)

    # Ans: 54
    ropes = [20, 4, 8, 2]
    print Solution().minCost(ropes)

    # Ans: 224
    ropes = [1, 2, 5, 10, 35, 89]
    print Solution().minCost(ropes)

    # AnsL 20
    ropes = [2, 2, 3, 3]
    print Solution().minCost(ropes)


if __name__ == '__main__':
    main()
