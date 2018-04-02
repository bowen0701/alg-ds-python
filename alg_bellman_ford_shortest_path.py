from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def bellman_ford(w_graph_d, start_vertex):
    """Bellman-Ford algorithm for weighted / negative graph.
    """
    pass


def main():
    w_graph_d = {
        's': {'a': 2, 'b': 6},
        'a': {'b': 3, 'c': 1},
        'b': {'a': -5, 'd': 2},
        'c': {'b': 1, 'e': 4, 'f': 2},
        'd': {'c': 3, 'f': 2},
        'e': {},
        'f': {'e': 1}
    }
    start_vertex = 's'
   

if __name__ == '__main__':
    main()
