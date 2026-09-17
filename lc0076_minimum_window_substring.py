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
    def minWindow(self, s: str, t: str) -> str:
        """
        Time complexity: O(m+n), where m = len(s), n = len(t).
        Space complexity: O(m+n).
        """
        from collections import Counter

        # How many more of each char the window still needs.
        # Positive = still needed, 0 = exactly satisfied, negative = surplus.
        # Counter also defaults to 0 for non-t chars (acts as defaultdict(int)).
        t_char_count_d = Counter(t)

        # Number of t-chars still missing from the window.
        n_missing = len(t)

        min_left = 0
        min_len = float('inf')

        left = 0

        # Expand window by moving right.
        for right in range(len(s)):
            # If this char is still needed (count > 0), one fewer char is missing.
            if t_char_count_d[s[right]] > 0:
                n_missing -= 1

            # Always decrement: surplus chars go negative, which is harmless.
            t_char_count_d[s[right]] -= 1

            # Contract window from left while all t-chars are satisfied.
            while n_missing == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left

                # Restore count for the char leaving the window.
                t_char_count_d[s[left]] += 1

                # If count goes positive, this char is missing again.
                if t_char_count_d[s[left]] > 0:
                    n_missing += 1

                left += 1

        return s[min_left:min_left + min_len] if min_len < float('inf') else ""


def main():
    # Output: "BANC"
    s = "ADOBECODEBANC"
    t = "ABC"
    print(SolutionCharCountDictTwoPointers().minWindow(s, t))

    # OutputL "ABBBBBBBBBA"
    s = "ABBBBBBBBBA"
    t = "AA"
    print(SolutionCharCountDictTwoPointers().minWindow(s, t))


if __name__ == '__main__':
    main()
