from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsited_d, clock, ccid_d, ccid):
    clock += 1
    previsited_d[v] = clock
    ccid_d[v] = ccid
    return previsited_d, clock, ccid_d, ccid


def _postvisit(v, postvisited_d, clock):
    clock += 1
    postvisited_d[v] = clock
    return postvisited_d, clock


def _dfs_explore(v, graph_adj_d, visited_d, 
                 previsited_d, postvisited_d, clock, ccid_d, ccid):
    visited_d[v] = True

    previsited_d, clock, ccid_d, ccid = _previsit(
        v, previsited_d, clock, ccid_d, ccid)
   
    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            visited_d, previsited_d, postvisited_d, clock, ccid_d, ccid = (
                _dfs_explore(v_neighbor, graph_adj_d, visited_d,
                             previsited_d, postvisited_d, clock, ccid_d, ccid))
    
    postvisited_d, clock = _postvisit(v, postvisited_d, clock)
    
    return visited_d, previsited_d, postvisited_d, clock, ccid_d, ccid


def dfs(graph_adj_d):
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = 0
    previsited_d = {}
    postvisited_d = {}
    ccid = 1
    ccid_d = {}
    for v in graph_adj_d.keys():
        if not visited_d[v]:
            visited_d, previsited, postvisited_d, clock, ccid_d, ccid = (
                _dfs_explore(v, graph_adj_d, visited_d, 
                             previsited_d, postvisited_d, clock, ccid_d, ccid))
    return previsited_d, postvisited_d


def _transpose_graph(graph_adj_d):
    tr_graph_adj_d = {v: [] for v in graph_adj_d.keys()}
    for v in graph_adj_d.keys():
        for v_neighbor in graph_adj_d[v]:
            tr_graph_adj_d[v_neighbor].append(v)
    return tr_graph_adj_d


def _decrease_postvisit_vertices(postvisited_d):
    tr_postvisited_d = {postvisited_d[k]: k for k in postvisited_d.keys()}
    dec_postvisited_ls = []
    for pv in reversed(sorted(tr_postvisited_d.keys())):
        dec_postvisited_ls.append(tr_postvisited_d[pv])
    return dec_postvisited_ls


def strongly_connected_components(graph_adj_d):
    """Strongly connected components for graph.

    Procedure:
      - Call (Depth First Search) DFS on graph G to 
        compute finish times for each vertex.
      - Compute the transpose graph G^T of graph G.
      - Call DFS on G^T, but in the main loop of DFS,
        feed the vertex in the decreasing order of postvisit times.
      - Output the vertices of each tree in the DFS forest as
        separate strongly connected components.
    """
    previsited_d, postvisited_d = dfs(graph_adj_d)
    tr_graph_adj_d = _transpose_graph(graph_adj_d)
    dec_postvisited_ls = _decrease_postvisit_vertices(postvisited_d)

    tr_visited_d = {v: False for v in tr_graph_adj_d}
    clock = 0
    tr_previsited_d = {}
    tr_postvisited_d = {}
    sccid = 1
    sccid_d = {}
    for v in dec_postvisited_ls:
        if not tr_visited_d[v]:
            (tr_visited_d, tr_previsited_d, tr_postvisited_d, 
             clock, sccid_d, sccid) = _dfs_explore(
                v, tr_graph_adj_d, tr_visited_d, 
                tr_previsited_d, tr_postvisited_d, clock, sccid_d, sccid)
            sccid += 1

    return (sccid_d, previsited_d, postvisited_d, 
            tr_graph_adj_d, dec_postvisited_ls)


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

    (sccid_d, previsited_d, postvisited_d, 
     tr_graph_adj_d, dec_postvisited_ls) = strongly_connected_components(graph_adj_d)

    print('previsited_d: {}'.format(previsited_d))
    print('postvisited_d: {}'.format(postvisited_d))
    print('tr_graph_adj_d: {}'.format(tr_graph_adj_d))
    print('dec_postvisited_ls: {}'.format(dec_postvisited_ls))

    print('Strongly connect components: {}'.format(sccid_d))





if __name__ == '__main__':
    main()
