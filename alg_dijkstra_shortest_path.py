from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def dijkstra(weighted_graph_d, start_vertex):
    """Dijkstra algorithm for weighted graph.

    Finds shortest path in a weighted graph from a particular node 
    to all vertices that are reachable from it.
    """
    pass

def main():
    weighted_graph_d = {
        'u': {'v': 2, 'w': 5, 'x': 1},
        'v': {'u': 2, 'w': 3, 'x': 2},
        'w': {'u': 5, 'v': 3, 'x': 3, 'y': 1, 'z': 5},
        'x': {'u': 1, 'v': 2, 'w': 3, 'y': 1},
        'y': {'w': 1, 'x': 1, 'z': 1},
        'z': {'w': 5, 'y': 1}
    }
    start_vertex = 'x'
    print('weighted_graph_d: {}'.format(weighted_graph_d))
    print('Dijkstra shortest path from {}:'.format(start_vertex))
    shortest_path_d, vertex_lookup_d = dijkstra(
        weighted_graph_d, start_vertex)
    print('shortest_path_d: {}'.format(shortest_path_d))
    print('vertex_lookup_d: {}'.format(vertex_lookup_d))

if __name__ == '__main__':
    main()
