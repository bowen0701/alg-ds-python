"""Leetcode 347. Top K Frequent Elements

URL: https://leetcode.com/problems/top-k-frequent-elements/

Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n),
where n is the array's size.
"""

from typing import List


class SolutionNubmerFreqDictBruteForce:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass


class SolutionNumberFreqDictSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n*logn), where n is the number of nums.
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Create num->freq dict.
        num_freq_d = defaultdict(int)

        for n in nums:
            num_freq_d[n] += 1

        # Sort num->freq dict by freq. 
        sorted_num_freqs = sorted(
            num_freq_d.items(), key=lambda x: x[1], reverse=True
        )

        # Take the top k num.
        topk_nums = [num for (num, freq) in sorted_num_freqs[:k]]
        return topk_nums


class SolutionNumberFreqDictMaxHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n*logn), where n is the number of nums.
        Space complexity: O(n).
        """
        from collections import defaultdict
        import heapq

        # Create num->freq dict.
        num_freq_d = defaultdict(int)

        for n in nums:
            num_freq_d[n] += 1

        # Push (freq, num) to max_heap.
        maxheap = []

        for (num, freq) in num_freq_d.items():
            heapq.heappush(maxheap, (-freq, num))

        # Pop the first k from max_heap.
        result = []
        for i in range(k):
            result.append(heapq.heappop(maxheap)[1])

        return result


class SolutionNumberFreqDictMinHeap:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n*log(k)), where n is the number of nums.
        Space complexity: O(k).
        """
        from collections import defaultdict, deque
        import heapq

        num_freq_d = defaultdict(int)
        for n in nums:
            num_freq_d[n] += 1

        # Push (freq, num) to min heap.
        minheap = []

        for num, freq in num_freq_d.items():
            heapq.heappush(minheap, (freq, num))

            if len(minheap) > k:
                heapq.heappop(minheap)

        # Pop number from minheap and collect result.
        result = deque([])
        while minheap:
            (freq, num) = heapq.heappop(minheap)
            result.appendleft(num)

        return list(result)


class SolutionNumberFreqDictBucketSort:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time complexity: O(n), where n is the number of nums.
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Create num->freq dict.
        num_freq_d = defaultdict(int)
        for num in nums:
            num_freq_d[num] += 1

        # Create a buck array with length n + 1.
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in num_freq_d.items():
            buckets[freq].append(num)

        # Get the top k frequent numbers.
        result = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

        return result


def main():
    import time

    # Output: [1,2]
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    start_time = time.time()
    print(SolutionNumberFreqDictSort().topKFrequent(nums, k))
    print(f"NumberFreqDictSort: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictMaxHeap().topKFrequent(nums, k))
    print(f"NumberFreqDictMaxHeap: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictMinHeap().topKFrequent(nums, k))
    print(f"NumberFreqDictMinHeap: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictBucketSort().topKFrequent(nums, k))
    print(f"NumberFreqDictBucketSort: {time.time() - start_time}")

    # Output: [1]
    nums = [1]
    k = 1

    start_time = time.time()
    print(SolutionNumberFreqDictSort().topKFrequent(nums, k))
    print(f"NumberFreqDictSort: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictMaxHeap().topKFrequent(nums, k))
    print(f"NumberFreqDictMaxHeap: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictMinHeap().topKFrequent(nums, k))
    print(f"NumberFreqDictMinHeap: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictBucketSort().topKFrequent(nums, k))
    print(f"NumberFreqDictBucketSort: {time.time() - start_time}")

    # Output: [1,2,5,3,7,6,4,8,10,11]
    nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    k = 10

    start_time = time.time()
    print(SolutionNumberFreqDictSort().topKFrequent(nums, k))
    print(f"NumberFreqDictSort: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictMaxHeap().topKFrequent(nums, k))
    print(f"NumberFreqDictMaxHeap: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictMinHeap().topKFrequent(nums, k))
    print(f"NumberFreqDictMinHeap: {time.time() - start_time}")

    start_time = time.time()
    print(SolutionNumberFreqDictBucketSort().topKFrequent(nums, k))
    print(f"NumberFreqDictBucketSort: {time.time() - start_time}")


if __name__ == '__main__':
    main()
