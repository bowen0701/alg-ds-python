from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsited_d, clock):
    clock[0] += 1
    previsited_d[v] = clock[0]


def _postvisit(v, postvisited_d, clock):
    clock[0] += 1
    postvisited_d[v] = clock[0]


def _dfs_visit(v, graph_adj_d, visited_d, 
               previsited_d, postvisited_d, clock, dag_bool):
    visited_d[v] = True
    _previsit(v, previsited_d, clock)

    for v_neighbor in graph_adj_d[v]:
        if (visited_d[v_neighbor]):
            # If v_neighbor was visited.
            if (previsited_d[v_neighbor] < previsited_d[v] and 
                not v_neighbor in postvisited_d):
                # If v's neighbor is visited before v, then not DAG.
                dag_bool[0] = False
        else:
            # If v_neighbor is not visited yet.
            _dfs_visit(v_neighbor, graph_adj_d, visited_d, 
                       previsited_d, postvisited_d, clock, dag_bool)

    _postvisit(v, postvisited_d, clock)


def dag(graph_adj_d):
    """Check Directed Acyclic Graph (DAG) by the DFS"""
    visited_d = {v: False for v in graph_adj_d.keys()}
    previsited_d = {}
    postvisited_d = {}
    clock = [0]
    dag_bool = [True]

    for v in graph_adj_d.keys():
        if not visited_d[v] and dag_bool:
            _dfs_visit(v, graph_adj_d, visited_d, 
                       previsited_d, postvisited_d, clock, dag_bool)

    return dag_bool[0]


def main():
    # DAG's adjacency dictionary.
    dag_adj_d = {
        'A': ['B', 'F'],
        'B': ['C', 'D', 'F'],
        'C': ['D'],
        'D': ['E', 'F'],
        'E': ['F'],
        'F': []
    }
    print('dag_adj_d: {}'.format(dag_adj_d))
    print('Is DAG: {}'.format(dag(dag_adj_d)))

    # non-DAG's adjacency dictionary.
    nondag_adj_d = {
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['A', 'C'],
        'D': ['B', 'C']
    }
    print('nondag_adj_d: {}'.format(nondag_adj_d))
    print('Is DAG: {}'.format(dag(nondag_adj_d)))


if __name__ == '__main__':
    main()
