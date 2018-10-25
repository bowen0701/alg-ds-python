from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _dfs_visit_stack(v, graph_adj_d, visited_ls):
    """DFS visit using stack.

    Ref: https://www.youtube.com/watch?v=or9xlA3YYzo
    """
    visited_ls.append(v)

    visit_stack = []
    visit_stack.append(v)
    while visit_stack:
        if set(graph_adj_d[visit_stack[-1]]) - set(visited_ls):
            for v_neighbor in graph_adj_d[visit_stack[-1]]:
                if v_neighbor not in visited_ls:
                    visited_ls.append(v_neighbor)
                    visit_stack.append(v_neighbor)
                    break
        else:
            visit_stack.pop()
    return visited_ls


def dfs(graph_adj_d):
    """Depth first search by iteration algorithm using stack.

    Time complexity for G(V, E): O(|V|+|E|).
    """
    visited_ls = []
    for v in graph_adj_d.keys():
        if v not in visited_ls:
            visited_ls = _dfs_visit_stack(v, graph_adj_d, visited_ls)
    return visited_ls


def main():
    # Connected graph by adjacency dictionary.
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
    print('Graph:\n{}'.format(graph_adj_d))

    print('Start DFS by stack:')
    visited_ls = dfs(graph_adj_d)
    print('visited_ls: {}'.format(visited_ls))


if __name__ == '__main__':
    main()
