from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from collections import defaultdict
from itertools import product


def _build_word_ladder_graph(words):
    w_neighbors_d = defaultdict(list)
    graph_d = defaultdict(set)

    # Create buckets of words that are different by one letter.
    for w in words:
        # For each letter in w, create its bucket.
        for i in xrange(len(w)):
            bucket = '{0}_{1}'.format(w[:i], w[i+1:])
            w_neighbors_d[bucket].append(w)

    # Add vertices and edges for words in the same buckets.
    for bucket, w_neighbors in w_neighbors_d.items():
        w_pairs = ((w1, w2) 
                   for w1, w2 in product(w_neighbors, repeat=2) 
                   if w1 != w2)

        for w1, w2 in w_pairs:
            graph_d[w1].add(w2)
            graph_d[w2].add(w1)

    return graph_d


def word_ladder(words, start_word, end_word):
    """Word ladder by BFS.

    Time complexity: O(WLW^2) + O(W+W^2)= O(W^3L) + O(W^2).
    Space complexity: O(W^2).
    """
    # Create graph with words connected to others which .
    words_graph = _build_word_ladder_graph(words)

    # Create distance dict.
    distance_d = {w: float('inf') for w in words_graph}
    distance_d[start_word] = 0

    # Apply BFS with queue for shortest path from start_word to end_word.
    queue = [start_word]

    while queue:
        visit_word = queue.pop()
        for neighbor_word in words_graph[visit_word]:
            # If neighbor_word is not visited.
            if distance_d[neighbor_word] == float('inf'):
                queue.insert(0, neighbor_word)
                distance_d[neighbor_word] = distance_d[visit_word] + 1

    return distance_d[end_word]


def main():
    words = ["hit", "hot", "dot", "dog", "lot", "log", "cog"]
 
    # "hit" -> "hot" -> "dot" -> "dog" -> "cog": 4
    start_word = 'hit'
    end_word = 'cog'
    print(word_ladder(words, start_word, end_word))


if __name__ == '__main__':
    main()
