from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from collections import defaultdict
from itertools import product

from alg_breadth_first_search import traverse_bfs

WORDS_FILE = 'four_letter_words.txt'


def read_words():
    """Read words file with producing a generator."""
    with open(WORDS_FILE) as f:
        for line in f:
            # Skip the end line symbol.
            yield line[:-1]


def build_word_ladder_graph(words):
    vertex_dict = defaultdict(list)
    graph_dict = defaultdict(set)

    # Create buckets of words that are different by one letter.
    for word in words:
        for i in xrange(len(word)):
            bucket = '{0}_{1}'.format(word[:i], word[i+1:])
            # if bucket in vertex_dict:
            #   vertex_dict[bucket].append(word)
            # else:
            #   vertex_dict[bucket] = list(word)
            vertex_dict[bucket].append(word)

    # Add vertices and edges for words in the same buckets.
    for bucket, neighbors_ls in vertex_dict.items():
        word_pairs_tuple = (
            ((word1, word2) 
             for word1, word2 in product(neighbors_ls, repeat=2) 
             if word1 != word2))
        
        for word1, word2 in word_pairs_tuple:
            graph_dict[word1].add(word2)
            graph_dict[word2].add(word1)

    return graph_dict


def main():
    words = read_words()
    words_graph = build_word_ladder_graph(words)
    print(words_graph)

    start_word = 'ACID'
    end_word = 'EYED'
    traverse_bfs(words_graph, start_word, end_word)

if __name__ == '__main__':
    main()
