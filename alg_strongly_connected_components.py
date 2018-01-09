from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsited_d, clock):
    clock += 1
    previsited_d[v] = clock
    return previsited_d, clock


def _postvisit(v, postvisited_d, clock):
    clock += 1
    postvisited_d[v] = clock
    return postvisited_d, clock


def _dfs_explore(v, graph_adj_d, visited_d, 
                 previsited_d, postvisited_d, clock):
    previsited_d, clock = _previsit(v, previsited_d, clock)
    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            visited_d, previsited_d, postvisited_d, clock = (
                _dfs_explore(v_neighbor, graph_adj_d, visited_d,
                             previsited_d, postvisited_d, clock))
    postvisited_d, clock = _postvisit(v, postvisited_d, clock)
    return visited_d, previsited_d, postvisited_d, clock


def dfs(graph_adj_d):
    visited_d = {v: False for v in graph_adj_d.keys()}
    previsited_d = {}
    postvisited_d = {}
    clock = 0
    for v in graph_adj_d.keys():
        if not visited_d[v]:
            visited_d, previsited, postvisited_d, clock = (
                _dfs_explore(v, graph_adj_d, visited_d, 
                             previsited_d, postvisited_d, clock))
    return previsited_d, postvisited_d


def _transpose_graph(graph_adj_d):
    tr_graph_adj_d = {v: [] for v in graph_adj_d.keys()}
    for v in graph_adj_d.keys():
        for v_neighbor in graph_adj_d[v]:
            tr_graph_adj_d[v_neighbor].append(v)
    return tr_graph_adj_d


def _decrease_postvisit_vertex():
    pass


def strongly_connected_components():
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
    dec_postvisited_ls = _decrease_postvisit_vertex(postvisited_d)
    visited_d = {v: False for v in tr_graph_adj_d}
    sccid_d = {}
    sccid = 0
    for v in dec_postvisited_ls:
        visited_d, sccid_d = _dfs_explore(tr_graph_adj_d, visited_d, sccid_d)
        sccid += 1
    return sccid_d


def main():
    # 3 strongly connected graphs: {A, B, D, E, G}, {C}, {F, H, I}.
    graph_adj_d = {
        'A': ['B'],
        'B': ['C', 'E'],
        'C': ['C', 'F'],
        'D': ['B', 'G'],
        'E': ['A', 'D'],
        'F': ['H'],
        'G': ['E'],
        'H': ['I'],
        'I': ['F']
    }

    # print(_transpose_graph(graph_adj_d))
    # strongly_connected_components(adj_dict)

if __name__ == '__main__':
    main()
