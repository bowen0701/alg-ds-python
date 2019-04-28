"""Leetcode 347. Top K Frequent Elements
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

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_d = {}

        for n in nums:
            if n in freq_d:
                freq_d[n] += 1
            else:
                freq_d[n] = 1
                
        sorted_freq_ls = sorted(
            freq_d.items(), key=lambda x: x[1], reverse=True)
        topk_ls = [t[0] for t in sorted_freq_ls[:k]]
        return topk_ls


def main():
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    # Output: [1,2]
    print Solution().topKFrequent(nums, k)

    nums = [1]
    k = 1
    # Output: [1]
    print Solution().topKFrequent(nums, k)

    nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    k = 10
    # Output: [1,2,5,3,7,6,4,8,10,11]
    print Solution().topKFrequent(nums, k)


if __name__ == '__main__':
    main()
