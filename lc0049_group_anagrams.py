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

class SolutionDict(object):
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
        # Store in a dict with sorted string->string array.  
        anagrams_d = {}

        for s in strs:
            # Get sorted string as key.
            k = ''.join(sorted(s))

            if anagrams_d.get(k):
                anagrams_d[k].append(s)
            else:
                anagrams_d[k] = [s]

        return anagrams_d.values()


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print SolutionDict().groupAnagrams(strs)


if __name__ == '__main__':
    main()
