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

class SolutionNaive(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        # Pop the shortest string as baseline.
        lens = [len(s) for s in strs]
        min_len = min(lens)
        for i, s in enumerate(strs):
            if len(s) == min_len:
                base_str = strs.pop(i)
                break

        # Iterate through baseline string's char to check common prefix.
        prefix = ''
        for i, char in enumerate(base_str):
            common_bool = True
            for s in strs:
                if char != s[i]:
                    common_bool = False
                    break
            
            if common_bool:
                prefix = ''.join([prefix, char])
            else:
                break

        return prefix


def main():
    strs = ["flower", "flow", "flight"]
    print SolutionNaive().longestCommonPrefix(strs)

    strs = ["dog", "racecar", "car"]
    print SolutionNaive().longestCommonPrefix(strs)


if __name__ == '__main__':
    main()
