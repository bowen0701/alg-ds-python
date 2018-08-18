from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsit_d, clock, ccid, ccid_d):
    clock += 1
    previsit_d[v] = clock
    ccid_d[v] = ccid
    return previsit_d, clock, ccid_d


def _postvisit(v, postvisit_d, clock):
    clock += 1
    postvisit_d[v] = clock
    return postvisit_d, clock


def _dfs_explore(v, graph_adj_d, visited_d, 
                 previsit_d, postvisit_d, clock, ccid, ccid_d):
    """DFS explore by recursion."""
    visited_d[v] = True
    previsit_d, clock, ccid_d = _previsit(v, previsit_d, clock, ccid, ccid_d)

    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            visited_d, previsit_d, postvisit_d, clock, ccid_d = (
                _dfs_explore(v_neighbor, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, clock, ccid, ccid_d))
    
    postvisit_d, clock = _postvisit(v, postvisit_d, clock)
    
    return visited_d, previsit_d, postvisit_d, clock, ccid_d


def undirected_graph_connected_components(graph_adj_d):
    """Connected components for undirected graph by DFS.

    Time complexity for graph G(V, E): O(|V|+|E|). 
    """
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = 0
    previsit_d = {}
    postvisit_d = {}

    # Connected component ID.
    ccid = 0
    ccid_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            ccid += 1
            visited_d, previsit_d, postvisit_d, clock, ccid_d = (
                _dfs_explore(v, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, clock, ccid, ccid_d))

    return ccid_d, previsit_d, postvisit_d


def main():
    # Undirected graph by adjacency dictionary, with connected component = 1.
    # graph_adj_d = {
    #     'A': ['B', 'F'],
    #     'B': ['A', 'C', 'G'],
    #     'C': ['B', 'D', 'G', 'H'],
    #     'D': ['C', 'E', 'H'],
    #     'E': ['D', 'I'],
    #     'F': ['A', 'G'],
    #     'G': ['B', 'C', 'F', 'H'],
    #     'H': ['C', 'D', 'G', 'I'],
    #     'I': ['E', 'H']
    # }

    # Undirected graph with connected component = 2.
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

    ccid_d, previsit_d, postvisit_d = undirected_graph_connected_components(graph_adj_d)
    print('ccid_d: {}'.format(ccid_d))
    print('previsit_d: {}'.format(previsit_d))
    print('postvisit_d: {}'.format(postvisit_d))


if __name__ == '__main__':
    main()
