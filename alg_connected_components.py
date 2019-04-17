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
               previsit_d, postvisit_d, clock, ccid, ccid_d):
    """DFS visit by recursion."""
    visited_d[v] = True
    ccid_d[v] = ccid

    _previsit(v, previsit_d, clock)

    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            _dfs_visit(v_neighbor, graph_adj_d, visited_d, 
                       previsit_d, postvisit_d, clock, ccid, ccid_d)
    
    _postvisit(v, postvisit_d, clock)
    

def connected_components(graph_adj_d):
    """Connected components for undirected graph G(V, E) by the DFS.

    Time complexity: O(|V|+|E|).
    Space complexity: O(|V|).
    """
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = [0]
    previsit_d = {}
    postvisit_d = {}

    # Connected component ID.
    ccid = 0
    ccid_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            ccid += 1
            _dfs_visit(v, graph_adj_d, visited_d, 
                       previsit_d, postvisit_d, clock, ccid, ccid_d)

    return ccid_d, previsit_d, postvisit_d


def main():
    # Undirected graph with connected components = 2.
    graph_adj_d = {
        'A': ['B', 'F'],
        'B': ['A', 'G'],
        'D': ['E', 'H'],
        'E': ['D', 'I'],
        'F': ['A', 'G'],
        'G': ['B', 'F'],
        'H': ['D', 'I'],
        'I': ['E', 'H']
    }

    ccid_d, previsit_d, postvisit_d = connected_components(graph_adj_d)
    print('ccid_d: {}'.format(ccid_d))
    print('previsit_d: {}'.format(previsit_d))
    print('postvisit_d: {}'.format(postvisit_d))


if __name__ == '__main__':
    main()
