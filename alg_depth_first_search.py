from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def dfs():
    """Depth first search by iteration algorithm using stack."""
    pass


def dfs_recur():
    """Depth first search by recursion algorithm."""
    pass


def main():
    # Connected graph by adjacency dictionary.
    graph_adjacency_dict = {
        'A': ['B', 'D'],
        'B': ['C', 'D'],
        'C': [],
        'D': ['E'],
        'E': ['B', 'F'],
        'F': ['C'],
    }
    print('Graph:\n{}'.format(graph_adjacency_dict))

if __name__ == '__main__':
    main()
