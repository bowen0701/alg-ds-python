from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsit_d, clock):
    clock[0] += 1
    previsit_d[v] = clock[0]


def _postvisit(v, postvisit_d, clock):
    clock[0] += 1
    postvisit_d[v] = clock[0]


def _dfs_visit(v, graph_adj_d, visited_d, 
               previsit_d, postvisit_d, clock):
    """DFS visit by recursion."""
    visited_d[v] = True
    _previsit(v, previsit_d, clock)

    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            _dfs_visit(v_neighbor, graph_adj_d, visited_d, 
                       previsit_d, postvisit_d, clock)
    
    _postvisit(v, postvisit_d, clock)


def dfs(graph_adj_d):
    """Depth First Search (DFS) by recursion algorithm.

    Time complexity for graph G(V, E): O(|V|+|E|). 
    """
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = [0]
    previsit_d = {}
    postvisit_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            # If vertex is not visited, re-start the DFS visit.
            _dfs_visit(v, graph_adj_d, visited_d, 
                       previsit_d, postvisit_d, clock)

    return previsit_d, postvisit_d


def main():
    # Undirected graph by adjacency list:
    graph_adj_d = {
        'A': ['B', 'D', 'G'],
        'B': ['A', 'E', 'F'],
        'C': ['F', 'H'],
        'D': ['A', 'F'],
        'E': ['B', 'G'],
        'F': ['B', 'C', 'D'],
        'G': ['A', 'E'],
        'H': ['C']
    }
    print('Graph:\n{}'.format(graph_adj_d))

    print('Start DFS by recursion.')
    previsit_d, postvisit_d = dfs(graph_adj_d)
    print('previsit_d: {}'.format(previsit_d))
    print('postvisit_d: {}'.format(postvisit_d))


if __name__ == '__main__':
    main()
