from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from ds_min_binary_heap_vertices import MinBinaryHeapVertices


def prim(w_graph_d):
    """Prim's algorithm for minimum spanning tree 
    in undirected weighted graph.

    Time complexity for graph G(V, E): O((|V|+|E|)log(|V|)).
    """
    min_pq = MinBinaryHeapVertices()

    key_d = {v: np.inf for v in w_graph_d.keys()}
    previous_d = {v: None for v in w_graph_d.keys()}
    visited_d = {v: False for v in w_graph_d.keys()}

    # Pick an arbitrary vertex as start.
    s = list(w_graph_d.keys())[0]
    visited_d[s] = True
    key_d[s] = 0
    min_pq.insert([key_d[s], s])

    while min_pq.heap_size > 0:
        k, v = min_pq.extract_min()
        visited_d[v] = True

        for v_neighbor in w_graph_d[v].keys():
            if (not visited_d[v_neighbor] and
                key_d[v_neighbor] > w_graph_d[v][v_neighbor]):
                key_d[v_neighbor] = w_graph_d[v][v_neighbor]
                previous_d[v_neighbor] = v
                min_pq.insert([key_d[v_neighbor], v_neighbor])

    return key_d, previous_d, visited_d


def main():
    w_graph_d = {
        'a': {'b': 1, 'd': 4, 'e': 3},
        'b': {'a': 1, 'd': 4, 'e': 2},
        'c': {'e': 4, 'f': 5},
        'd': {'a': 4, 'b': 4, 'e': 4},
        'e': {'a': 3, 'b': 2, 'c': 4, 'd': 4, 'f': 7},
        'f': {'c': 5, 'e': 7}
    }
    print('w_graph_d:\n{}'.format(w_graph_d))

    print('Prim\'s minimum spanning tree:')
    key_d, previous_d, visited_d = prim(w_graph_d)
    print('key_d: {}'.format(key_d))
    print('previous_d: {}'.format(previous_d))
    print('visited_d: {}'.format(visited_d))


if __name__ == '__main__':
    main()
