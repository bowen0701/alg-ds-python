"""Leetcode 387. First Unique Character in a String
Easy

URL: https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.
s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""

class SolutionDict(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Create a dict for char->index i. If repeated, char -> -1.
        from collections import defaultdict

        char_idx_d = defaultdict(int)

        for i, c in enumerate(s):
            if c not in char_idx_d:
                char_idx_d[c] = i
            else:
                char_idx_d[c] = -1

        # Iterate through items. If idx is valid (not - 1), update min_idx.
        min_idx = float('inf')

        for char, idx in char_idx_d.items():
            if idx != -1:
                min_idx = min(min_idx, idx)

        # Check mix_id is valid or not.
        if min_idx != float('inf'):
            return min_idx
        else:
            return -1


def main():
    # Ans: 0
    s = 'leetcode'
    print SolutionDict().firstUniqChar(s)

    # Ans: 2
    s = 'loveleetcode'
    print SolutionDict().firstUniqChar(s)

    # Ans: -1
    s = 'aabbccdd'
    print SolutionDict().firstUniqChar(s)


if __name__ == '__main__':
    main()
