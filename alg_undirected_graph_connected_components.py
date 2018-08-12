from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsit_d, ccid_d, ccid, clock):
    clock += 1
    previsit_d[v] = clock
    ccid_d[v] = ccid
    return previsit_d, ccid_d, clock


def _postvisit(v, postvisit_d, clock):
    clock += 1
    postvisit_d[v] = clock
    return postvisit_d, clock


def _dfs_explore(v, graph_adj_d, visited_d, 
                 previsit_d, postvisit_d, ccid_d, ccid, clock):
    """DFS explore by recursion."""
    visited_d[v] = True
    previsit_d, ccid_d, clock = _previsit(v, previsit_d, ccid_d, ccid, clock)

    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            visited_d, previsit_d, postvisit_d, ccid_d, clock = (
                _dfs_explore(v_neighbor, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, ccid_d, ccid, clock))
    
    postvisit_d, clock = _postvisit(v, postvisit_d, clock)
    
    return visited_d, previsit_d, postvisit_d, ccid_d, clock


def undirected_graph_connected_components(graph_adj_d):
    """Connected components for undirected graph by DFS.

    Time complexity for graph G(V, E): O(|V|+|E|). 
    """
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = 0
    previsit_d = {}
    postvisit_d = {}

    # Connected component ID.
    ccid = 1
    ccid_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            visited_d, previsit_d, postvisit_d, ccid_d, clock = (
                _dfs_explore(v, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, ccid_d, clock, ccid))
            ccid += 1

    return ccid_d, previsit_d, postvisit_d


def main():
    # Undirected graph by adjacency dictionary.
    # TODO: Define Undirected graph.
    graph_adj_d = {
        'A': ['B', 'F'],
        'B': ['A', 'C', 'G'],
        'C': ['B', 'D', 'G', 'H'],
        'D': ['C', 'E', 'H'],
        'E': ['B', 'F'],
        'F': ['C'],
    }
    print('Graph:\n{}'.format(graph_adj_d))

    print('Find connected components by DFS.')
    ccid_d, previsit_d, postvisit_d = undirected_graph_connected_components(graph_adj_d)
    print('ccid_d: {}'.format(ccid_d))
    print('previsit_d: {}'.format(previsit_d))
    print('postvisit_d: {}'.format(postvisit_d))


if __name__ == '__main__':
    main()
