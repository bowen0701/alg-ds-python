"""Leetcode 49. Group Anagrams
Medium

URL: https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
- All inputs will be in lowercase.
- The order of your output does not matter.
"""

class SolutionSortedDict(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]

        Output Limit Exceede.

        Time complexity: O(n*klogk), where
          - n is the length of strs,
          - k is the lenght of the longest string.
        Space complexity: O(n).
        """
        from collections import defaultdict

        # Store in a dict with sorted string->string list.  
        anagrams_d = defaultdict(list)

        for s in strs:
            # Use sorted string as dict key.
            k = ''.join(sorted(s))
            anagrams_d[k].append(s)

        return anagrams_d.values()


def main():
    # Output:
    # [
    #   ["ate","eat","tea"],
    #   ["nat","tan"],
    #   ["bat"]
    # ]
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print SolutionSortedDict().groupAnagrams(strs)


if __name__ == '__main__':
    main()
