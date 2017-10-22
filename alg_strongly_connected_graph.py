from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def dfs_recur():
	pass

def traverse_dfs_recur():
	pass

def transpose_graph():
	pass

def strongly_connected_graph():
    """Find strongly connected graphs by Kosaraju's Algorithm."""


def main():
    adjacency_dict = {
        'A': {'B'},
        'B': {'C', 'E'},
        'C': {'C', 'F'},
        'D': {'B', 'G'},
        'E': {'A', 'D'},
        'F': {'H'},
        'G': {'E'},
        'H': {'I'},
        'I': {'F'}
    }

if __name__ == '__main__':
    main()
