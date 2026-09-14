"""Leetcode 239. Sliding Window Maximum
Hard

URL: https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of
size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window
moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

from typing import List


class SolutionBrute:
    def maxSlidingWindow(
        self,
        nums: List[int],
        k: int,
    ) -> List[int]:
        """
        Time complexity: O(n * k), where n is the length of nums.
        Space complexity: O(n), O(k) for slice + O(n-k+1) for result.
        """
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            result.append(max(nums[i:i + k]))

        return result


class SolutionMaxHeap:
    def maxSlidingWindow(
        self,
        nums: List[int],
        k: int,
    ) -> List[int]:
        """
        Time complexity: O(n * logn), where n is the length of nums.
          - Each element is pushed/popped at most once, each O(logn).
          - Worst case: all elements stay in heap (e.g., ascending input).
        Space complexity: O(n), lazy deletion so all elements may stay in heap.
        """
        import heapq

        n = len(nums)
        result = []

        # Max heap: store (-value, index) since Python has min heap.
        max_heap = []

        for right in range(n):
            heapq.heappush(max_heap, (-nums[right], right))

            # Window is full: record max.
            if right >= k - 1:
                # If the max element's index is before the left boundary, 
                # it's outside the window → pop it.
                while max_heap[0][1] < right - k + 1:
                    heapq.heappop(max_heap)

                result.append(-max_heap[0][0])

        return result


class SolutionMonotonicDeque:
    def maxSlidingWindow(
        self,
        nums: List[int],
        k: int,
    ) -> List[int]:
        """
        Time complexity: O(n), where n is the length of nums.
          - Each element is pushed/popped from deque at most once.
        Space complexity: O(k) for deque.
        """
        from collections import deque

        n = len(nums)
        result = []

        # Deque: stores indices of monotonic decreasing elements. 
        dq = deque()

        for right in range(n):
            # Remove indices outside window.
            if dq and dq[0] < right - k + 1:
                dq.popleft()

            # Maintain decreasing order: remove smaller elements from back.
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            # Window is full: record max (front of deque).
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result


def main():
    # Output: [3,3,5,5,6,7]
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(SolutionBrute().maxSlidingWindow(nums, k))
    print(SolutionMaxHeap().maxSlidingWindow(nums, k))
    print(SolutionMonotonicDeque().maxSlidingWindow(nums, k))

    # Output: [1]
    nums = [1]
    k = 1
    print(SolutionBrute().maxSlidingWindow(nums, k))
    print(SolutionMaxHeap().maxSlidingWindow(nums, k))
    print(SolutionMonotonicDeque().maxSlidingWindow(nums, k))

    # Output: [3, 3, 2, 5]
    nums = [1, 3, 1, 2, 0, 5]
    k = 3
    print(SolutionBrute().maxSlidingWindow(nums, k))
    print(SolutionMaxHeap().maxSlidingWindow(nums, k))
    print(SolutionMonotonicDeque().maxSlidingWindow(nums, k))


if __name__ == '__main__':
    main()
