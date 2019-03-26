from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from ds_min_heap_attribute import MinHeapAttribute


def dijkstra_shortest_path(w_graph_d, v_start):
    """Dijkstra algorithm for singel-source shortest path problem 
    in a "weighted" graph G(V, E) by BFS with min binary heap.

    Time complexity: O(|V|+|E|)log(|V|).
    Space complexity: O(|V|).
    """
    min_pq = MinHeapAttribute()

    distance_d = {v: np.inf for v in w_graph_d.keys()}
    visited_d = {v: False for v in w_graph_d.keys()}
    
    min_pq.add([0, v_start])
    distance_d[v_start] = 0
    visited_d[v_start] = True

    while min_pq.size > 0:
        k, v = min_pq.extract_min()
        visited_d[v] = True

        for v_neighbor in w_graph_d[v].keys():
            if (not visited_d[v_neighbor] and 
                distance_d[v_neighbor] > 
                    distance_d[v] + w_graph_d[v][v_neighbor]):
                distance_d[v_neighbor] = distance_d[v] + w_graph_d[v][v_neighbor]
                min_pq.add([distance_d[v_neighbor], v_neighbor])

    return distance_d


def main():
    w_graph_d = {
        's': {'a': 2, 'b': 6},
        'a': {'b': 3, 'c': 1},
        'b': {'a': 5, 'd': 2},
        'c': {'b': 1, 'e': 4, 'f': 2},
        'd': {'c': 3, 'f': 2},
        'e': {},
        'f': {'e': 1}
    }
    start_vertex = 's'
    
    print('Dijkstra shortest path:')
    distance_d = dijkstra_shortest_path(w_graph_d, start_vertex)
    print('distance_d: {}'.format(distance_d))
   

if __name__ == '__main__':
    main()
