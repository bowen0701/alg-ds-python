from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from collections import defaultdict

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
    """Traverse graph by Depth First Search by Iteration with Stack."""
    connect_bool = False
    for vertex, path_ls in dfs(adjacency_dict, start_vertex):
        if vertex == end_vertex:
            connect_bool = True
            print(' -> '.join(path_ls))
            break

    if not connect_bool:
        print('No path from {0} to {1}'.format(start_vertex, end_vertex))


def dfs_recur(adjacency_dict, start_vertex, 
              visited_set, visit_time, path_dict):
    """Depth First Search by Recursion.

    Use the followings to track discover & dinish times
      - path_dict[vertex]['discover']
      - path_dict[vertex]['finish']
    """
    visited_set.add(start_vertex)
    visit_time[0] += 1
    path_dict[start_vertex]['discover'] = visit_time[0]

    for neighbor_vertex in adjacency_dict[start_vertex]:
        if neighbor_vertex not in visited_set:
            dfs_recur(adjacency_dict, neighbor_vertex, 
                      visited_set, visit_time, path_dict)

    visit_time[0] += 1
    path_dict[start_vertex]['finish'] = visit_time[0]

def traverse_dfs_recur(adjacency_dict, start_vertex):
    """Traverse graph by Depth First Search by Recursion.

    To make sure all vertices in connected or disconnected graph
    are visited, we start from start_vertex to iterate all vertices.
    """
    visited_set = set()
    visit_time = [0]
    path_dict = defaultdict(dict)
    
    vertices_ls = [start_vertex]
    other_vertices_ls = adjacency_dict.keys()
    other_vertices_ls.remove(start_vertex)
    vertices_ls.extend(other_vertices_ls)
    for vertex in vertices_ls:
        if vertex not in visited_set:
            dfs_recur(adjacency_dict, vertex, 
                      visited_set, visit_time, path_dict)

    for vertex in path_dict:
        print('{0}:\n{1}'.format(vertex, path_dict[vertex]))


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

    # print('For dfs by iteration:')
    # traverse_dfs(adjacency_dict, start_vertex, end_vertex)

    print('For dfs by recursion:')
    traverse_dfs_recur(adjacency_dict, start_vertex)

if __name__ == '__main__':
    main()
