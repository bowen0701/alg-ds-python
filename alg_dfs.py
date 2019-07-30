from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit(v, previsit_d, clock):
    clock[0] += 1
    previsit_d[v] = clock[0]


def _postvisit(v, postvisit_d, clock):
    clock[0] += 1
    postvisit_d[v] = clock[0]


def _dfs_recur_visit(v, graph_adj_d, visited_d, 
                     previsit_d, postvisit_d, clock):
    """DFS helper by recursion."""
    visited_d[v] = True
    _previsit(v, previsit_d, clock)

    for v_neighbor in graph_adj_d[v]:
        if not visited_d[v_neighbor]:
            _dfs_recur_visit(v_neighbor, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, clock)
    
    _postvisit(v, postvisit_d, clock)


def dfs_recur(graph_adj_d):
    """Depth First Search (DFS) in graph G(V, E) by recursion algorithm.

    Time complexity: O(|V|+|E|).
    Space complexity: O(|V|).
    """
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = [0]
    previsit_d = {}
    postvisit_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            # If vertex is not visited, re-start the DFS visit.
            _dfs_recur_visit(v, graph_adj_d, visited_d, 
                             previsit_d, postvisit_d, clock)

    return previsit_d, postvisit_d


def _dfs_iter_visit(v, graph_adj_d, visited_d, 
                    previsit_d, postvisit_d, clock):
    """DFS helper by iteration using stack."""
    _previsit(v, previsit_d, clock)
    visited_d[v] = True

    stack = []
    stack.append(v)

    while stack:
        visited_set = {v for v in visited_d if visited_d[v] is True}
        if set(graph_adj_d[stack[-1]]) - visited_set:
            # Travel stack last node's neighbor, if not visited, 
            # add the neighbor to visited and directly go to next traverse.
            for v_neighbor in graph_adj_d[stack[-1]]:
                if not visited_d[v_neighbor]:
                    _previsit(v_neighbor, previsit_d, clock)
                    visited_d[v_neighbor] = True
                    stack.append(v_neighbor)
                    break
        else:
            # When there is no neighbor to travel, pop out stack last node,
            # and step back for further traverse.
            v_pop = stack.pop()
            _postvisit(v_pop, postvisit_d, clock)
    return previsit_d, postvisit_d


def dfs_iter(graph_adj_d):
    """Depth First Search (DFS) in graph G(V, E) 
    by iteration algorithm using stack.

    Time complexity: O(|V|+|E|).
    Space complexity: O(|V|).
    """
    visited_d = {v: False for v in graph_adj_d.keys()}
    clock = [0]
    previsit_d = {}
    postvisit_d = {}

    for v in graph_adj_d.keys():
        if not visited_d[v]:
            _dfs_iter_visit(v, graph_adj_d, visited_d, 
                            previsit_d, postvisit_d, clock)
    return previsit_d, postvisit_d


def main():
    # Undirected graph by adjacency list:
    graph_adj_d = {
        'A': ['B', 'D', 'G'],
        'B': ['A', 'E', 'F'],
        'C': ['F', 'H'],
        'D': ['A', 'F'],
        'E': ['B', 'G'],
        'F': ['B', 'C', 'D'],
        'G': ['A', 'E'],
        'H': ['C']
    }

    print('DFS by recursion:')
    previsit_d, postvisit_d = dfs_recur(graph_adj_d)
    print('previsit_d: {}'.format(previsit_d))
    print('postvisit_d: {}'.format(postvisit_d))

    print('DFS by iteration:')
    previsit_dd, postvisit_dd = dfs_iter(graph_adj_d)
    print('previsit_dd: {}'.format(previsit_dd))
    print('postvisit_dd: {}'.format(postvisit_dd))


if __name__ == '__main__':
    main()
