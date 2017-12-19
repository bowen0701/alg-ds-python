from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def dfs_stack():
    """Depth first search by iteration algorithm using stack."""
    pass


# TODO: Pass variables into helper functions.

def _previsit(v):
    clock += 1
    previsit_d[v] = clock
    ccnum_d[v] = ccid

def _postvisit(v):
    clock += 1
    postvisit_d[v] = clock

def _dfs_explore(v):
    visited_d[v] = True
    _previsit(v)
    for neighbor_v in graph_adj_d[v]:
        if not visited_d[neighbor_v]:
            _dfs_explore(neighbor_v)
    _postvisit(v)

def dfs(graph_adj_d):
    """Depth first search by recursion algorithm."""
    clock = 0
    ccid = 1
    previsit_d = {}
    ccnum_d = {}
    postvisit_d = {}
    visited_d = {v: False for v in graph_adj_d.keys()}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            _dfs_explore(v)
            ccid += 1

    print('previsit_d: {}'.format(previsit_d))
    print('postvisit_d: {}'.format(postvisit_d))
    print('ccnum_d: {}'.format(ccnum_d))


def main():
    # Connected graph by adjacency dictionary.
    graph_adj_d = {
        'A': ['B', 'D'],
        'B': ['C', 'D'],
        'C': [],
        'D': ['E'],
        'E': ['B', 'F'],
        'F': ['C'],
    }
    print('Graph:\n{}'.format(graph_adj_d))

    dfs(graph_adj_d)

if __name__ == '__main__':
    main()
