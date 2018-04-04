from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import numpy as np


def update_distance(v, v_neighbor, 
                    w_graph_d, distance_d, previous_d):
    if (distance_d[v_neighbor] > 
            distance_d[v] + w_graph_d[v][v_neighbor]):
        distance_d[v_neighbor] = (
            distance_d[v] + w_graph_d[v][v_neighbor])
        previous_d[v_neighbor] = v
    return distance_d, previous_d 


def bellman_ford(w_graph_d, start_vertex):
    """Bellman-Ford algorithm for weighted / negative graph."""
    distance_d = {v: np.inf for v in w_graph_d.keys()}
    previous_d = {v: None for v in w_graph_d.keys()}

    distance_d[start_vertex] = 0

    n = len(w_graph_d.keys())
    # Run through |V| - 1 times.
    for i in xrange(1, n):
        # Run through all edges.
        for v in w_graph_d.keys():
            for v_neighbor in w_graph_d[v].keys():
                distance_d, previous_d = update_distance(
                    v, v_neighbor, w_graph_d, distance_d, previous_d)
    
    # Check negative cycle.
    _distance_d = distance_d.copy()
    _previous_d = previous_d.copy()

    for v in w_graph_d.keys():
        for v_neighbor in w_graph_d[v].keys():
            _distance_d, _previous_d = update_distance(
                v, v_neighbor, w_graph_d, _distance_d, _previous_d)
            if _distance_d != distance_d:
                raise ValueError('Negative cycle exists.')

    return distance_d, previous_d


def main():
    w_graph_d = {
        's': {'a': 2, 'b': 6},
        'a': {'b': 3, 'c': 1},
        'b': {'a': -2, 'd': 2},
        'c': {'b': 1, 'e': 4, 'f': 2},
        'd': {'c': 3, 'f': 2},
        'e': {},
        'f': {'e': 1}
    }
    start_vertex = 's'

    distance_d, previous_d = bellman_ford(w_graph_d, start_vertex)
    print('distance_d: {}'.format(distance_d))
    print('previous_d: {}'.format(previous_d))
   

if __name__ == '__main__':
    main()
