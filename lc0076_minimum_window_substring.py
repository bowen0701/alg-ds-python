"""Leetcode 76. Minimum Window Substring
Hard

URL: https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty
string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest
window of s only has one 'a', return empty string.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

class SolutionCharCountDictTwoPointers:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        Time complexity: O(m+n), where
          - m: lenght of s,
          - n: lenght of t.
        Space complexity: O(m+n).
        """
        from collections import Counter

        # Remaining need: positive = still needed, 0 = satisfied, negative = surplus.
        # Counter acts as defaultdict(int), so non-t chars default to 0.
        t_char_count_d = Counter(t)

        # Total chars still needed to complete a valid window.
        t_counter = len(t)

        min_left = 0
        min_len = float('inf')

        left, right = 0, 0

        # Expand window by moving right.
        while right < len(s):
            # Only decrement t_counter when this char is genuinely needed (count > 0).
            # Non-t chars have count 0; surplus t-chars have count 0 or below.
            if t_char_count_d[s[right]] > 0:
                t_counter -= 1

            # Always decrement: tracks how many more of this char the window needs.
            # Non-t chars go negative (e.g., -1), which is harmless.
            t_char_count_d[s[right]] -= 1
            right += 1

            # Window contains all of t: shrink from left to find minimum.
            while t_counter == 0:
                if right - left < min_len:
                    min_len = right - left
                    min_left = left

                # Restore count for the char leaving the window.
                t_char_count_d[s[left]] += 1

                # If count goes positive, this char is now needed again.
                # Non-t chars go from negative back toward 0, never triggering this.
                if t_char_count_d[s[left]] > 0:
                    t_counter += 1

                left += 1

        if min_len < float('inf'):
            return s[min_left:(min_left + min_len)]
        else:
            return ''


def main():
    # Output: "BANC"
    s = "ADOBECODEBANC"
    t = "ABC"
    print(SolutionCharCountDictTwoPointers().minWindow(s, t))

    s = "ABBBBBBBBBA"
    t = "AA"
    print(SolutionCharCountDictTwoPointers().minWindow(s, t))


if __name__ == '__main__':
    main()
