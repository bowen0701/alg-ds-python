"""Leetcode 269. Alien Dictionary (Premium)
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
    def _build_graph(self, words, graph, indegrees):
        # Set graph keys as all chars.
        for w in words:
            for c in w:
                graph[c] = set()

        # Build graph and in-degree in order of words with different chars.
        for i in range(1, len(words)):
            word_from = words[i - 1]
            word_to = words[i]

            min_len = min(len(word_from), len(word_to))
            for j in range(min_len):
                char_from = word_from[j]
                char_to = word_to[j]

                if char_from != char_to:
                    if char_to not in graph[char_from]:
                        graph[char_from].add(char_to)
                        indegrees[char_to] += 1

                        # Break after get the 1st different char.
                        break

    def _topological_sort(self, graph, indegrees):
        # Build order string based on in-degrees by Kahn's algorithm.

        from collections import deque

        # Put char into zero in-degree queue if its in-degree is 0.
        zero_indegree_queue = deque([])

        for c in graph:
            if indegrees[c] == 0:
                zero_indegree_queue.appendleft(c)

        order_chars = []

        while zero_indegree_queue:
            # Put zero in-degree char in order chars.
            c = zero_indegree_queue.pop()
            order_chars.append(c)

            # Visit zero in-degree char c's neighbors and decrement their 
            # in-degrees, since c is removed.
            for c_neighbor in graph[c]:
                indegrees[c_neighbor] -= 1

                # If c's neighbor has zero in-degrees, append to queue.
                if indegrees[c_neighbor] == 0:
                    zero_indegree_queue.appendleft(c_neighbor)

        order_string = ''.join(order_chars)
        return order_string

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str

        Time complexity: O(n), where n is the length of words.
        Space complexity: O(1), since we have fixed number of chars.
        """
        # Apply Kahn's algorithm for topological sort for string order.

        from collections import defaultdict

        # Edge case.
        if not words or not words[0]:
            return ''

        # Build graph dict for char_from->set(char_to),
        # and indegrees list for char's in-degree.
        graph = defaultdict(set)
        indegrees = defaultdict(int)

        # Build graph and in-degrees.
        self._build_graph(words, graph, indegrees)

        # Run Topological Sort to create string order.
        order_str = self._topological_sort(graph, indegrees)

        # Check if length of string order is the same as that of graph keys.
        if len(order_str) == len(graph.keys()):
            return order_str
        else:
            return ''


def main():
    # Output: "wertf"
    words = [
      "wrt",
      "wrf",
      "er",
      "ett",
      "rftt"
    ]
    print SolutionTopologicalSort().alienOrder(words)

    # Output: "zx"
    words = [
      "z",
      "x"
    ]
    print SolutionTopologicalSort().alienOrder(words)

    # Output: ""
    words = [
      "z",
      "x",
      "z"
    ] 
    print SolutionTopologicalSort().alienOrder(words)


if __name__ == '__main__':
    main()
