"""Leetcode 14. Longest Common Prefix.
Easy

URL: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""

class SolutionIter(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        Time complexity: O(m*n), where
          - m is the maximum length of strs, and
          - n is the length of "minimum" string.
        Space complexity: O(1).
        """
        if not strs:
            return ''

        # Choose str 0 as the baseline.
        prefix = ''

        for pos, c in enumerate(strs[0]):
            for j in range(1, len(strs)):
                # Check if position is out of boundary or not matched. 
                if pos >= len(strs[j]) or c != strs[j][pos]:
                    return prefix

            prefix += c

        return prefix


def main():
    # Output: "fl"
    strs = ["flower", "flow", "flight"]
    print SolutionIter().longestCommonPrefix(strs)

    # Output: ""
    strs = ["dog", "racecar", "car"]
    print SolutionIter().longestCommonPrefix(strs)


if __name__ == '__main__':
    main()
