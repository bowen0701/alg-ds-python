"""Leetcode 295. Find Median from Data Stream
Hard

URL: https://leetcode.com/problems/find-median-from-data-stream/

Median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:
- void addNum(int num) - Add a integer number from the data stream to 
  the data structure.
- double findMedian() - Return the median of all elements so far.
 
Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 
Follow up:
- If all integer numbers from the stream are between 0 and 100, 
  how would you optimize it?
- If 99% of all integer numbers from the stream are between 0 and 100, 
  how would you optimize it?
"""

import heapq


class MedianFinder(object):
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
        if not self.small_maxheap or num < -self.small_maxheap[0]:
            heapq.heappush(self.small_maxheap, -num)
        else:
            heapq.heappush(self.large_minheap, num)

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
        if len(self.small_maxheap) == len(self.large_minheap):
            return ((-1 * self.small_maxheap[0]) + self.large_minheap[0]) / 2.0
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
    print obj.findMedian()
    obj.addNum(3)
    print obj.findMedian()


if __name__ == '__main__':
    main()
