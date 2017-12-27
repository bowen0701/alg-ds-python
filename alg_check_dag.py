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
                 previsited_d, postvisited_d, clock, dag_bool):
    visited_d[v] = True
    previsited_d, clock = _previsit(v, previsited_d, clock)
    for v_neighbor in graph_adj_d[v]:
        print('{0} -> {1}'.format(v, v_neighbor))
        if (visited_d[v_neighbor] and
            previsited_d[v] > previsited_d[v_neighbor] and 
            not v_neighbor in postvisited_d):
            dag_bool = False
        if not visited_d[v_neighbor]:
            previsited_d, postvisited_d, clock, dag_bool = (
                _dfs_explore(v_neighbor, graph_adj_d, visited_d, 
                             previsited_d, postvisited_d, clock, dag_bool))
    postvisited_d, clock = _postvisit(v, postvisited_d, clock)
    return previsited_d, postvisited_d, clock, dag_bool

def check_dag(graph_adj_d):
    """Check Directed Acyclic Graph (DAG)."""
    visited_d = {v: False for v in graph_adj_d.keys()}
    previsited_d = {}
    postvisited_d = {}
    clock = 0
    dag_bool = True
    for v in graph_adj_d.keys():
        if not visited_d[v] and dag_bool:
            previsited_d, postvisited_d, clock, dag_bool = (
            _dfs_explore(v, graph_adj_d, visited_d, 
                         previsited_d, postvisited_d, clock, dag_bool))
    return dag_bool


def main():
    # Graph adjacency dictionary for DAG.
    dag_adj_d = {
        'A': ['D'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E', 'G'],
        'E': ['J'],
        'F': ['G'],
        'G': ['I'],
        'I': ['J'],
        'J': []
    }
    print('dag_adj_d: {}'.format(dag_adj_d))
    print('Is DAG: {}'.format(check_dag(dag_adj_d)))

    # Graph adjacency dictionary for non-DAG.
    nondag_adj_d = {
        'A': ['B'],
        'B': ['C', 'D'],
        'C': ['A', 'C'],
        'D': ['B', 'C']
    }
    print('nondag_adj_d: {}'.format(nondag_adj_d))
    print('Is DAG: {}'.format(check_dag(nondag_adj_d)))

if __name__ == '__main__':
    main()
