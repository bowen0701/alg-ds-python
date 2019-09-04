"""Leetcode 3. Longest Substring Without Repeating Characters
Medium

URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without 
repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
  Note that the answer must be a substring, "pwke" is a 
  subsequence and not a substring.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(k), k is the number of characters.
        """
        start = 0
        max_len = 0
        char_d = {}

        for i, c in enumerate(s):
            if c in char_d and start <= char_d[c]:
                # When repeating char is visited.
                start = char_d[c] + 1
            else:
                # If not, update max length.
                max_len = max(max_len, i - start + 1)

            # Always update char dict for every char in s.
            char_d[c] = i

        return max_len


def main():
    # Example 1: "abcabcbb" -> 3 ("abc")
    s = "abcabcbb"
    print('For {0}: {1}'.format(s, Solution().lengthOfLongestSubstring(s)))

    # Example 2: "bbbbb" -> 1 ("b")
    s = "bbbbb"
    print('For {0}: {1}'.format(s, Solution().lengthOfLongestSubstring(s)))

    # Example 3: "pwwkew" -> 3 ("wke")
    s = "pwwkew"
    print('For {0}: {1}'.format(s, Solution().lengthOfLongestSubstring(s)))


if __name__ == '__main__':
    main()
