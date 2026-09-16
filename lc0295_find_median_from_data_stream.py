"""Leetcode 295. Find Median from Data Stream
Hard

URL: https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size
of the list is even, there is no middle value, and the median is the
mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to
  the data structure.
- double findMedian() returns the median of all elements so far.
  Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input: ["MedianFinder", "addNum", "addNum", "findMedian", "addNum",
"findMedian"]
[[], [1], [2], [], [3], []]
Output: [null, null, null, 1.5, null, 2.0]

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before
  calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow up:
- If all integer numbers from the stream are in the range [0, 100],
  how would you optimize it?
- If 99% of all integer numbers from the stream are in the range
  [0, 100], how would you optimize it?
"""

import heapq


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small_maxheap = []
        self.large_minheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Store small half and large half to max heap and min heap, respectively. 
        if not self.small_maxheap or num < -self.small_maxheap[0]:
            # To obtain a max heap, push negative item to a negative min heap.
            heapq.heappush(self.small_maxheap, -num)
        else:
            heapq.heappush(self.large_minheap, num)

        # Rebalance two heaps if one is much bigger than the other by 2.
        if len(self.small_maxheap) - len(self.large_minheap) == 2:
            pop_item = -heapq.heappop(self.small_maxheap)
            heapq.heappush(self.large_minheap, pop_item)
        elif len(self.small_maxheap) - len(self.large_minheap) == -2:
            pop_item = heapq.heappop(self.large_minheap)
            heapq.heappush(self.small_maxheap, -pop_item)

    def findMedian(self):
        """
        :rtype: float
        """
        # If two heaps are balanced, return mean of their peek as median. 
        if len(self.small_maxheap) == len(self.large_minheap):
            return ((-1 * self.small_maxheap[0]) + self.large_minheap[0]) / 2.0
        # If no balanced, return bigger heap's peek.
        elif len(self.small_maxheap) > len(self.large_minheap):
            return -self.small_maxheap[0]
        elif len(self.small_maxheap) < len(self.large_minheap):
            return self.large_minheap[0]


def main():
    # Your MedianFinder object will be instantiated and called as such:
    # obj = MedianFinder()
    # obj.addNum(num)
    # param_2 = obj.findMedian()
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())


if __name__ == '__main__':
    main()
