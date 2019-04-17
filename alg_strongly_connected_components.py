from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _reverse_graph(graph_adj_d):
    rev_graph_adj_d = {v: [] for v in graph_adj_d.keys()}

    for v in graph_adj_d.keys():
        for v_neighbor in graph_adj_d[v]:
            rev_graph_adj_d[v_neighbor].append(v)

    return rev_graph_adj_d


def _previsit(v, previsited_d, clock):
    clock[0] += 1
    previsited_d[v] = clock[0]


def _postvisit(v, postvisited_d, clock):
    clock[0] += 1
    postvisited_d[v] = clock[0]


def _dfs_visit(v, graph_adj_d, visited_d, 
                 previsited_d, postvisited_d, clock, ccid, ccid_d):
    visited_d[v] = True
    ccid_d[v] = ccid

    _previsit(v, previsited_d, clock)
   
    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            _dfs_visit(v_neighbor, graph_adj_d, visited_d,
                       previsited_d, postvisited_d, clock, ccid, ccid_d)
    
    _postvisit(v, postvisited_d, clock)


def _dfs(graph_adj_d):
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = [0]
    previsited_d = {}
    postvisited_d = {}

    ccid = 0
    ccid_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            ccid += 1
            _dfs_visit(v, graph_adj_d, visited_d, 
                       previsited_d, postvisited_d, clock, ccid, ccid_d)

    return ccid_d, previsited_d, postvisited_d


def _decrease_postvisit_vertices(postvisited_d):
    tr_postvisited_d = {postvisited_d[k]: k for k in postvisited_d.keys()}
    dec_postvisited_ls = []

    for pv in reversed(sorted(tr_postvisited_d.keys())):
        dec_postvisited_ls.append(tr_postvisited_d[pv])

    return dec_postvisited_ls


def strongly_connected_components(graph_adj_d):
    """Strongly connected components for directed graph G(V, E) by DFS.

    Procedure:
    - Obtain the reverse graph G^R of graph G.
    - Call DFS on G^R in the decreasing order of postvisit number found
      in step 1.
    - Output the labeled connected components found in step 2.

    Time complexity: O(|V| + |E|).
    Space complexity: O(|V|).
    """
    visited_d = {v: False for v in graph_adj_d}
    clock = [0]
    previsited_d = {}
    postvisited_d = {}
    
    sccid = 0
    sccid_d = {}

    rev_graph_adj_d = _reverse_graph(graph_adj_d)
    _, _, rev_postvisited_d = _dfs(rev_graph_adj_d)
    dec_rev_postvisited_ls = _decrease_postvisit_vertices(
        rev_postvisited_d)

    for v in dec_rev_postvisited_ls:
        if not visited_d[v]:
            sccid += 1
            _dfs_visit(v, graph_adj_d, visited_d, 
                       previsited_d, postvisited_d, clock, sccid, sccid_d)

    return (sccid_d, previsited_d, postvisited_d)


def main():
    # 4 strongly connected graphs: {A, B, E}, {C, D}, {F, G}, {H}.
    graph_adj_d = {
        'A': ['B'],
        'B': ['C', 'E', 'F'],
        'C': ['D', 'G'],
        'D': ['C', 'H'],
        'E': ['A', 'F'],
        'F': ['G'],
        'G': ['F', 'H'],
        'H': ['H']
    }

    (sccid_d, previsited_d, postvisited_d) = (
        strongly_connected_components(graph_adj_d))

    print('previsited_d: {}'.format(previsited_d))
    print('postvisited_d: {}'.format(postvisited_d))
    print('Strongly connect components: {}'.format(sccid_d))


if __name__ == '__main__':
    main()
