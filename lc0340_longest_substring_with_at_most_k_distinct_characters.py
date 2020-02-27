"""Leetcode 340. Longest Substring with At Most K Distinct Characters
Hard

URL: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string, find the length of the longest substring T that contains at most k
distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""


class SolutionTwoPointerCharCountDictIter(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(k).
        """
        from collections import defaultdict

        # Apply sliding window with two pointers to increment dict:char->count.
        char_count_d = defaultdict(int)
        
        max_len = 0
        i = 0

        # Move right pointer j iteratively.
        for j in range(len(s)):
            # Increment char count for s[j].
            char_count_d[s[j]] += 1

            if len(char_count_d) > k:
                # If distinct char count > k, move i to decrement it for s[i].
                char_count_d[s[i]] -= 1
                if char_count_d[s[i]] == 0:
                    del char_count_d[s[i]]
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len


def main():
    # Output: 3
    s = "eceba"
    k = 2
    print SolutionTwoPointerCharCountDictIter().lengthOfLongestSubstringKDistinct(s, k)

    # Output: 2
    s = "aa"
    k = 1
    print SolutionTwoPointerCharCountDictIter().lengthOfLongestSubstringKDistinct(s, k)


if __name__ == '__main__':
    main()
