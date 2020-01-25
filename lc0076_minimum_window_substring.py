"""Leetcode 76. Minimum Window Substring
Hard

URL: https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
- If there is no such window in S that covers all characters in T, return the
  empty string "".
- If there is such window, you are guaranteed that there will always be only one
  unique minimum window in S.
"""

class SolutionCharCountDictTwoPointers(object):
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
        from collections import defaultdict

        # Use dict to collect t's char->count.
        t_char_count_d = defaultdict(int)
        for c in t:
            t_char_count_d[c] += 1

        # Track min left & len, and t_counter.
        min_left = 0
        min_len = float('inf')

        t_counter = len(t)

        # Apply two pointers with left & right from head as a window.
        left, right = 0, 0

        # In s, move right to increase window to satify t.
        while right < len(s):
            # If right char exits in t, decrement t_counter.
            if t_char_count_d[s[right]] > 0:
                t_counter -= 1

            # Decrement t_char_count_d and increment right.
            t_char_count_d[s[right]] -= 1
            right += 1

            # While window satisfies t, move left to shorten it.
            while t_counter == 0:
                # Update min_len and min_left if improve min_len.
                if right - left < min_len:
                    min_len = right - left
                    min_left = left

                # Before increment left, add back t_char_count_d & t_counter.
                t_char_count_d[s[left]] += 1
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
    print SolutionCharCountDictTwoPointers().minWindow(s, t)

    s = "ABBBBBBBBBA"
    t = "AA"
    print SolutionCharCountDictTwoPointers().minWindow(s, t)


if __name__ == '__main__':
    main()
