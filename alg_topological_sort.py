from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit():
    pass

def _postvisit():
    pass

def _dfs_explore():
    pass

def topological_sort():
    """Topological Sorting for Directed Acyclic Graph (DAG).

    To topologically sort a DAG, we simply do depth first search,
    then arrange DAG's vertices in decreasing postvisit order.
    """
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
