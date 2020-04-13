"""Leetcode 1046. Last Stone Weight
Easy

URL: https://leetcode.com/problems/last-stone-weight/

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.
Suppose the stones have weights x and y with x <= y.  
The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight
y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone
(or 0 if there are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value
of last stone.
"""

class SolutionMaxHeap(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int

        Time complexity: O(n*logn).
        Space complexity: O(n).
        """
        import heapq

        if not stones:
            return 0

        # Add stones in max heap (min heap with negative weights).
        max_stones = []
        for w in stones:
            heapq.heappush(max_stones, -w)

        # Iteratively smash stone pairs when have at least two.
        while len(max_stones) >= 2:
            stone1 = -heapq.heappop(max_stones)
            stone2 = -heapq.heappop(max_stones)

            if stone1 != stone2:
                heapq.heappush(max_stones, -(stone1 - stone2))

        if max_stones:
            return -max_stones[0]
        else:
            return 0


def main():
    # Output: 1.
    stones = [2,7,4,1,8,1]
    print SolutionMaxHeap().lastStoneWeight(stones)


if __name__ == '__main__':
    main()
