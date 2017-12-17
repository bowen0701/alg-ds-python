from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_stack import Stack


def dfs(adjacency_dict, start_vertex):
    """Depth First Search by Iteration using Stack."""
    ls_stack = Stack()
    ls_stack.push([start_vertex])
    visited_set = set([start_vertex])
    
    while ls_stack.size() > 0:
        # Take top vertex as the next start vertex.
        path_ls = ls_stack.peek()
        vertex = path_ls[-1]
        print('vertex: {}'.format(vertex))
        yield vertex, path_ls
        neighbor_vertices = adjacency_dict[vertex]
        if len(neighbor_vertices) > 0:
            neighbor_vertex = neighbor_vertices.pop()
            if neighbor_vertex not in path_ls:
                visited_set.add(neighbor_vertex)
                ls_stack.push(path_ls + [neighbor_vertex])
        else:
            ls_stack.pop()

def traverse_dfs(adjacency_dict, start_vertex, end_vertex):
    """Traverse graph by Depth First Search by Iteration with Stack."""
    connect_bool = False
    for vertex, path_ls in dfs(adjacency_dict, start_vertex):
        if vertex == end_vertex:
            connect_bool = True
            print(' -> '.join(path_ls))
            break

    if not connect_bool:
        print('No path from {0} to {1}'.format(start_vertex, end_vertex))


def dfs_recur(adjacency_dict, start_vertex, visited_set, discover_ls, finish_ls):
    """Depth First Search by Recursion."""
    visited_set.add(start_vertex)
    # path_ls.append(start_vertex)
    discover_ls.append(start_vertex)
    for neighbor_vertex in adjacency_dict[start_vertex]:
        if neighbor_vertex not in visited_set:
            dfs_recur(adjacency_dict, neighbor_vertex, visited_set, 
                      discover_ls, finish_ls)
    finish_ls.insert(0, start_vertex)

def traverse_dfs_recur(adjacency_dict):
    """Traverse graph by Depth First Search by Recursion.

    To make sure all vertices in connected or disconnected graph
    are visited, we start from start_vertex to iterate all vertices.
    """
    visited_set = set()
    # path_ls = []
    discover_ls = []
    finish_ls = []
    for vertex in adjacency_dict:
        if vertex not in visited_set:
            dfs_recur(adjacency_dict, vertex, visited_set, discover_ls, finish_ls)
    print('discover_ls: {}'.format(discover_ls))
    print('finish_ls: {}'.format(finish_ls))


def main():
    # Connected graph.
    conn_adjacency_dict = {
        'A': ['B', 'D'],
        'B': ['C', 'D'],
        'C': [],
        'D': ['E'],
        'E': ['B', 'F'],
        'F': ['C'],
    }

    # print('For dfs by iteration:')
    # start_vertex = 'A'
    # end_vertex = 'F'
    # traverse_dfs(conn_adjacency_dict, start_vertex, end_vertex)

    print('For dfs by recursion:')
    traverse_dfs_recur(conn_adjacency_dict)

if __name__ == '__main__':
    main()
