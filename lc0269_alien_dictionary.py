"""Leetcode 269. Alien Dictionary
Hard

URL: https://leetcode.com/problems/alien-dictionary

There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from
the dictionary, where words are sorted lexicographically by the rules of this
new language. Derive the order of letters in this language.

Example 1:
Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
Output: "wertf"
Example 2:
Input:
[
  "z",
  "x"
]
Output: "zx"

Example 3:
Input:
[
  "z",
  "x",
  "z"
] 
Output: "" 
Explanation: The order is invalid, so return "".

Note:
- You may assume all letters are in lowercase.
- You may assume that if a is a prefix of b, then a must appear before b in the 
  given dictionary.
- If the order is invalid, return an empty string.
- There may be multiple valid order of letters, return any one of them is fine.
"""

class SolutionTopologicalSort(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict

        # Edge case.
        if not words or not words[0]:
            return ''

        # Use dict to build graph: char_from->set(char_to).
        graph = defaultdict(set)

        # Use list to collect char's in-degree.
        indegrees = [0] * 26

        # Build graph and in-degrees.
        self.build_graph(words, graph, indegrees)

        # Run Topological Sort to create string order.
        str_order = self.topological_sort(graph, indegrees)

        # Check if length of string order is the same as that of graph keys.
        if len(str_order) == len(graph.keys()):
            return str_order
        else:
            return ''



def main():
    pass


if __name__ == '__main__':
    main()
