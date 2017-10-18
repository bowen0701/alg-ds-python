from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_stack import Stack


def dfs(adjacency_dict, start_vertex):
    ls_stack = Stack()
    ls_stack.push([start_vertex])
    visited_set = set([start_vertex])
    
    while ls_stack.size() > 0:
        # Take top vertex as the next start vertex.
        path_ls = ls_stack.peek()
        vertex = path_ls[-1]
        # print('path_ls: {}'.format(path_ls))
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
    connect_bool = False
    for vertex, path_ls in dfs(adjacency_dict, start_vertex):
        if vertex == end_vertex:
            connect_bool = True
            print(' -> '.join(path_ls))
            break

    if not connect_bool:
        print('No path from {0} to {1}'.format(start_vertex, end_vertex))


def dfs_recur():
    pass


def main():
    # Connected graph.
    adjacency_dict = {
        'A': {'B', 'D'},
        'B': {'C', 'D'},
        'C': {},
        'D': {'E'},
        'E': {'B', 'F'},
        'F': {'C'},
    }
    
    start_vertex = 'A'
    end_vertex = 'F'
    
    print('For dfs by iteration:')
    traverse_dfs(adjacency_dict, start_vertex, end_vertex)

    print('For dfs by recursion:')
    print('TODO')

if __name__ == '__main__':
    main()
