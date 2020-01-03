"""Leetcode 127. Word Ladder
Medium

URL: https://leetcode.com/problems/word-ladder/

Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord,
such that:

- Only one letter can be changed at a time.
- Each transformed word must exist in the word list.
- Note that beginWord is not a transformed word.

Note:
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.
- You may assume no duplicates in the word list.
- You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is
"hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList,
therefore no possible transformation.
"""

class SolutionBfs(object):
    def _buildWordsGraph(self, words):
        from collections import defaultdict
        from itertools import product

        # To build word graph, first build words_neighbors dict: bucket->list(words).
        words_neighbors = defaultdict(list)

        for w in words:
            for i in range(len(w)):
                # Create bucket of words that are different by one letter.
                bucket = '{0}_{1}'.format(w[:i], w[i+1:])
                words_neighbors[bucket].append(w)

        # Build words_graph dict: word->set(words).
        words_graph = defaultdict(set)

        for bucket, w_neighbors in words_neighbors.items():
            w_pairs = ((w1, w2) for (w1, w2) in product(w_neighbors, repeat=2)
                       if w1 != w2)

            for w1, w2 in w_pairs:
                words_graph[w1].add(w2)
                words_graph[w2].add(w1)

        return words_graph

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        Time complexity: O(WLW^2) + O(W+W^2)= O(W^3L) + O(W^2).
        Space complexity: O(W^2).
        """
        # Apply iterative BFS with queue for shortest lengths from start.
        # - Make words complete.
        # - Build words graph dict, based on words neighbors dict.
        # - Use lengths dict.

        from collections import defaultdict
        from collections import deque

        # If endWord is not in wordList, not possible to transform.
        if endWord not in wordList:
            return 0

        # Make words complete.
        words = wordList[:]
        words.append(beginWord)

        # Build words graph.
        words_graph = self._buildWordsGraph(words)

        # Use lengths dict.
        lengths = defaultdict(int)
        for w in words_graph:
            lengths[w] = float('inf')

        lengths[beginWord] = 1

        # Apply BFS with queue for shortest lengths.
        queue = deque([beginWord])

        while queue:
            w = queue.pop()

            # Start BFS if word neighbor is not visited yet.
            for w_neighbor in words_graph[w]:
                if lengths[w_neighbor] == float('inf'):
                    queue.appendleft(w_neighbor)
                    lengths[w_neighbor] = lengths[w] + 1

        return lengths[endWord]


def main():
    # Output: 5
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print SolutionBfs().ladderLength(beginWord, endWord, wordList)

    # Output: 0
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    print SolutionBfs().ladderLength(beginWord, endWord, wordList)

    # Output: 0
    beginWord = "hot"
    endWord = "dog"
    wordList = ["dog"]
    print SolutionBfs().ladderLength(beginWord, endWord, wordList)


if __name__ == '__main__':
    main()
