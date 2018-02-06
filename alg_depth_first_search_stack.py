from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v_visit, previsited_d, clock):
    clock += 1
    previsited_d[v_visit] = clock
    return previsited_d, clock


def _dfs_stack_explore(v, graph_adj_d, visited_d,
                       previsited_d, clock):
    visit_stack = []
    visit_stack.append(v)
    while visit_stack:
        v_visit = visit_stack.pop()
        visited_d[v_visit] = True
        previsited_d, clock = _previsit(v_visit, previsited_d, clock)
        for v_neighbor in graph_adj_d[v_visit]:
            if not visited_d[v_neighbor]:
                visit_stack.append(v_neighbor)
    return previsited_d


def dfs_stack(graph_adj_d):
    """Depth first search by iteration algorithm using stack."""
    visited_d = {v: False for v in graph_adj_d.keys()}
    previsited_d = {}
    clock = 0
    for v in graph_adj_d.keys():
        if not visited_d[v]:
            previsited_d = _dfs_stack_explore(
                v, graph_adj_d, visited_d, previsited_d, clock)
    return previsited_d


def main():
    # Connected graph by adjacency dictionary.
    graph_adj_d = {
        'A': ['B', 'D'],
        'B': ['C', 'D'],
        'C': [],
        'D': ['E'],
        'E': ['B', 'F'],
        'F': ['C'],
    }
    print('Graph:\n{}'.format(graph_adj_d))

    print('Start DFS by stack.')
    previsit_d = dfs_stack(graph_adj_d)
    print('previsit_d: {}'.format(previsit_d))


if __name__ == '__main__':
    main()
