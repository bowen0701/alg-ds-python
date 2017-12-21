from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def topological_sort():
    """Topological Sorting for Directed Acyclic Graph (DAG)."""
    pass


def main():
    # DAG.
    dag_adjacency_dict = {
        'A': ['D'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E', 'G'],
        'E': ['J'],
        'F': ['G'],
        'G': ['I'],
        'I': ['J'],
        'J': []
    }

if __name__ == '__main__':
    main()
