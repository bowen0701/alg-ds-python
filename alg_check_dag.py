from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit():
    pass

def _postvisit():
    pass

def _dfs_explore():
    pass

def check_dag():
    """Check Directed Acyclic Graph (DAG)."""
    pass


def main():
    # DAG.
    dag_adj_d = {
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
