"""Leetcode 1167 Minimum Cost to Connect Sticks (Premium)
Medium

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
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        # Apply min heap to iteratively connect two shortest sticks.
        import heapq

        if not sticks or len(sticks) == 1:
            return 0

        if len(sticks) == 2:
            return sum(sticks)

        min_cost = 0

        min_hq = sticks[:]
        heapq.heapify(min_hq)

        # Iteratively connect stick pair when at least two.
        while len(min_hq) >= 2:
            stick1 = heapq.heappop(min_hq)
            stick2 = heapq.heappop(min_hq)
            
            connected_stick = stick1 + stick2

            # Accumulate min cost with additional cost.
            min_cost += connected_stick

            # Push the additional cost to min heap.
            heapq.heappush(min_hq, connected_stick)

        return min_cost


def main():
    # Ans: 58
    ropes = [8, 4, 6, 12]
    print SolutionMinHeap().connectSticks(ropes)

    # Ans: 54
    ropes = [20, 4, 8, 2]
    print SolutionMinHeap().connectSticks(ropes)

    # Ans: 224
    ropes = [1, 2, 5, 10, 35, 89]
    print SolutionMinHeap().connectSticks(ropes)

    # AnsL 20
    ropes = [2, 2, 3, 3]
    print SolutionMinHeap().connectSticks(ropes)


if __name__ == '__main__':
    main()
