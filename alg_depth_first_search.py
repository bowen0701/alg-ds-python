from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsit_d, clock):
    clock += 1
    previsit_d[v] = clock
    return previsit_d, clock


def _postvisit(v, postvisit_d, clock):
    clock += 1
    postvisit_d[v] = clock
    return postvisit_d, clock


def _dfs_explore(v, graph_adj_d, visited_d, previsit_d, postvisit_d, clock):
    """Explore by recursion."""
    visited_d[v] = True
    previsit_d, clock = _previsit(v, previsit_d, clock)

    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            visited_d, previsit_d, postvisit_d, clock = (
                _dfs_explore(v_neighbor, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, clock))
    
    postvisit_d, clock = _postvisit(v, postvisit_d, clock)
    
    return visited_d, previsit_d, postvisit_d, clock


def dfs(graph_adj_d):
    """Depth first search by recursion algorithm.

    Time complexity for graph G(V, E): O(|V|+|E|). 
    """
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = 0
    previsit_d = {}
    postvisit_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            visited_d, previsit_d, postvisit_d, clock = (
                _dfs_explore(v, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, clock))

    return previsit_d, postvisit_d


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

    print('Start DFS by recursion.')
    previsit_d, postvisit_d = dfs(graph_adj_d)
    print('previsit_d: {}'.format(previsit_d))
    print('postvisit_d: {}'.format(postvisit_d))


if __name__ == '__main__':
    main()
