from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def dfs_recur(adj_dict, start_vertex, visited_set, 
              discover_ls, finish_ls):
    visited_set.add(start_vertex)
    discover_ls.append(start_vertex)
    for neighbor_vertex in adj_dict[start_vertex]:
        if neighbor_vertex not in visited_set:
            dfs_recur(adj_dict, neighbor_vertex, visited_set, 
                      discover_ls, finish_ls)
    finish_ls.insert(0, start_vertex)

def traverse_dfs_recur(adj_dict):
    visited_set = set()
    discover_ls = []
    finish_ls = []
    for vertex in adj_dict:
        if vertex not in visited_set:
            dfs_recur(adj_dict, vertex, visited_set, 
                      discover_ls, finish_ls)
    return discover_ls, finish_ls

def transpose_graph(adj_dict):
    tr_adj_dict = {}

    for vertex in adj_dict:
        tr_adj_dict[vertex] = []

    for vertex in adj_dict:
        for neighbor_vertex in adj_dict[vertex]:
            tr_adj_dict[neighbor_vertex].append(vertex)

    return tr_adj_dict

def strongly_connected_components(adj_dict):
    """Find strongly connected graphs by Kosaraju's Algorithm."""
    discover_ls, finish_ls = traverse_dfs_recur(adj_dict)
    print('discover_ls for G: {}'.format(discover_ls))
    print('finish_ls for G: {}'.format(finish_ls))

    tr_adj_dict = transpose_graph(adj_dict)
    print('G^T: {}'.format(tr_adj_dict))

    print('strongly connected components:')
    scc_visited_set = set()
    for vertex in finish_ls:
        scc_discover_ls = []
        scc_finish_ls = []
        if vertex not in scc_visited_set:
            dfs_recur(tr_adj_dict, vertex, scc_visited_set, 
                      scc_discover_ls, scc_finish_ls)
            print('scc_discover_ls: {}'.format(scc_discover_ls))


def main():
    # 3 strongly connected graphs: {A, B, D, E, G}, {C}, {F, H, I}.
    adj_dict = {
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

    strongly_connected_components(adj_dict)

if __name__ == '__main__':
    main()
