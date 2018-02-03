from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsit_d, ccid_d, clock, ccid):
    """Previsit method."""
    clock += 1
    previsit_d[v] = clock
    ccid_d[v] = ccid
    return previsit_d, clock


def _postvisit(v, postvisit_d, clock):
    """Postvisit method."""
    clock += 1
    postvisit_d[v] = clock
    return postvisit_d, clock


def _dfs_explore(v, graph_adj_d, visited_d, 
                 previsit_d, postvisit_d, ccid_d, clock, ccid):
    """Explore method by depth first search by recursion."""
    visited_d[v] = True
    previsit_d, clock = _previsit(v, previsit_d, ccid_d, clock, ccid)

    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            visited_d, previsit_d, postvisit_d, ccid_d, clock = (
                _dfs_explore(v_neighbor, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, ccid_d, clock, ccid))
    
    postvisit_d, clock = _postvisit(v, postvisit_d, clock)
    
    return visited_d, previsit_d, postvisit_d, ccid_d, clock


def dfs(graph_adj_d):
    """Depth first search by recursion algorithm.

    Args:
      graph_adj_d: A dict. Graph adjacency dictionary.

    Returns:
      previsit_d: A dict. Previsit time clock.
      postvisit_d: A dict. Postvisit time clock.
      ccid_d: A dict. Connected component number.
    """
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = 0
    previsit_d = {}
    postvisit_d = {}
    ccid = 1
    ccid_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            visited_d, previsit_d, postvisit_d, ccid_d, clock = (
            _dfs_explore(v, graph_adj_d, visited_d, 
                         previsit_d, postvisit_d, ccid_d, clock, ccid))
            ccid += 1

    return previsit_d, postvisit_d, ccid_d


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
                v, graph_adj_d, visited_d, 
                previsited_d, clock)
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

    print('Start DFS by recursion.')
    previsit_d, postvisit_d, ccid_d = dfs(graph_adj_d)
    print('previsit_d: {}'.format(previsit_d))
    print('postvisit_d: {}'.format(postvisit_d))
    print('ccid_d: {}'.format(ccid_d))

    print('Start DFS by stack.')
    previsit_d = dfs_stack(graph_adj_d)
    print('previsit_d: {}'.format(previsit_d))


if __name__ == '__main__':
    main()
