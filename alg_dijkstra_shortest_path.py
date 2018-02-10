from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import numpy as np


def dijkstra(weighted_graph_d, start_vertex):
    """Dijkstra algorithm for "weighted" graph.

    Finds shortest path in a weighted graph from a particular node 
    to all vertices that are reachable from it.
    """
    distance_d = {v: np.inf for v in weighted_graph_d.keys()}
    visited_d = {v: False for v in weighted_graph_d.keys()}
    
    distance_d[start_vertex] = 0
    visited_d[visited_d] = True
    pass


def main():
    weighted_graph_d = {
        's': {'a': 2, 'b': 6},
        'a': {'b': 3, 'c': 1},
        'b': {'a': 5, 'd': 2},
        'c': {'b': 1, 'e': 4, 'f': 2},
        'd': {'c': 3, 'f': 2},
        'e': {},
        'f': {'e': 1}
    }
    start_vertex = 's'
    print('weighted_graph_d: {}'.format(weighted_graph_d))
    print('Dijkstra shortest path from {}:'.format(start_vertex))
    

if __name__ == '__main__':
    main()
