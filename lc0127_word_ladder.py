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

class Solution(object):
    def _buildWordsGraph(self, words):
        from collections import defaultdict
        from itertools import product

        w_neighbors_d = defaultdict(list)
        graph_d = defaultdict(set)

        # Create bucket of words that are different by one letter.
        for w in words:
            for i in range(len(w)):
                bucket = '{0}_{1}'.format(w[:i], w[i+1:])
                w_neighbors_d[bucket].append(w)

        # Add graph's vertices and edges for words in the same buckets.
        for bucket, w_neighbors in w_neighbors_d.items():
            w_pairs = ((w1, w2) 
                       for (w1, w2) in product(w_neighbors, repeat=2)
                       if w1 != w2)
        
            for w1, w2 in w_pairs:
                graph_d[w1].add(w2)
                graph_d[w2].add(w1)

        return graph_d

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        Time complexity: O(WLW^2) + O(W+W^2)= O(W^3L) + O(W^2).
        Space complexity: O(W^2).
        """
        # If endWord is not in wordList, not possible to transform.
        if endWord not in wordList:
            return 0

        # Make words complete.
        words = wordList[:]
        words.append(beginWord)

        # Build words graph.
        words_graph = self._buildWordsGraph(words)

        # Make length dict.
        length_d = {w: float('inf') for w in words_graph}
        length_d[beginWord] = 1

        # Apply BFS with queue for shortest length.
        queue = [beginWord]

        while queue:
            visit_word = queue.pop()

            for neighbor_word in words_graph[visit_word]:
                # If neighbor word is not visited yet.
                if length_d[neighbor_word] == float('inf'):
                    queue.insert(0, neighbor_word)
                    length_d[neighbor_word] = length_d[visit_word] + 1

        if length_d.get(endWord):
            return length_d[endWord]
        else:
            return 0


def main():
    # Output: 5
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print Solution().ladderLength(beginWord, endWord, wordList)

    # Output: 0
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    print Solution().ladderLength(beginWord, endWord, wordList)

    # Output: 0
    beginWord = "hot"
    endWord = "dog"
    wordList = ["dog"]
    print Solution().ladderLength(beginWord, endWord, wordList)


if __name__ == '__main__':
    main()
