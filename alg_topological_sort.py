from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsited_d, clock):
    clock[0] += 1
    previsited_d[v] = clock[0]


def _postvisit(v, postvisited_d, clock):
    clock[0] += 1
    postvisited_d[v] = clock[0]


def _dfs_visit(v, dag_adj_d, visited_d,
               previsited_d, postvisited_d, clock):
    visited_d[v] = True
    _previsit(v, previsited_d, clock)

    for v_neighbor in dag_adj_d[v]:
        if not visited_d[v_neighbor]:
            _dfs_visit(v_neighbor, dag_adj_d, visited_d,
                       previsited_d, postvisited_d, clock)

    _postvisit(v, postvisited_d, clock)


def _decrease_postvisit_vertices(postvisited_d):
    tr_postvisited_d = {postvisited_d[k]: k for k in postvisited_d.keys()}
    dec_postvisited_ls = []
    for pv in reversed(sorted(tr_postvisited_d.keys())):
        # Arrange DAG vertices in decreasing postvisited id.
        dec_postvisited_ls.append(tr_postvisited_d[pv])
    return dec_postvisited_ls


def topological_sort(dag_adj_d):
    """Topological Sorting for DAG G(V, E) by the DFS.

    To topologically sort a DAG, 
    - we simply do depth first search,
    - then arrange DAG's vertices in decreasing order of postvisits.

    Time complexity: O(|V| + |E|).
    Space complexity: O(|V|).
    """
    visited_d = {v: False for v in dag_adj_d.keys()}
    previsited_d = {}
    postvisited_d = {}
    clock = [0]

    for v in dag_adj_d.keys():
        if not visited_d[v]:
            _dfs_visit(v, dag_adj_d, visited_d,
                       previsited_d, postvisited_d, clock)

    dec_postvisited_ls = _decrease_postvisit_vertices(postvisited_d)

    return dec_postvisited_ls


def main():
    # DAG.
    dag_adj_d = {
        'A': ['B', 'F'],
        'B': ['C', 'D', 'F'],
        'C': ['D'],
        'D': ['E', 'F'],
        'E': ['F'],
        'F': []
    }
    
    print(topological_sort(dag_adj_d))


if __name__ == '__main__':
    main()
