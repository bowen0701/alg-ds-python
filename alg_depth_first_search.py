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
        # print('vertex: {}'.format(vertex))
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
    for vertex, path_ls in dfs(adjacency_dict, start_vertex):
        if vertex == end_vertex:
            print(' -> '.join(path_ls))
            break


def _dfs_recur(adjacency_dict, start_vertex, path_ls):
    path_ls += [start_vertex]
    for neighbor_vertex in adjacency_dict[start_vertex]:
        if neighbor_vertex not in path_ls:
            _dfs_recur(adjacency_dict, neighbor_vertex, path_ls)

def dfs_recur(adjacency_dict, start_vertex):
    path_ls = []
    for start_vertex in adjacency_dict:
        if start_vertex not in path_ls:
            _dfs_recur(adjacency_dict, start_vertex, path_ls)
    return path_ls


def main():
    # Small word ladder graph.
    adjacency_dict = {
        'fool': {'cool', 'pool', 'foil', 'foul'},
        'foul': {'fool', 'foil'},
        'foil': {'fool', 'foul', 'fail'},
        'cool': {'fool', 'pool'},
        'fail': {'foil', 'fall'},
        'fall': {'fail', 'pall'},
        'pool': {'fool', 'cool', 'poll'},
        'poll': {'pool', 'pall', 'pole'},
        'pall': {'fall', 'pale', 'poll'},
        'pole': {'poll', 'pope', 'pale'},
        'pope': {'pole'},
        'pale': {'pall', 'pole', 'sale', 'page'},
        'sale': {'pale', 'sage'},
        'page': {'pale', 'sage'},
        'sage': {'sale', 'page'} 
    }
    
    start_vertex = 'fool'
    end_vertex = 'sage'
    
    print('For dfs by iteration:')
    traverse_dfs(adjacency_dict, start_vertex, end_vertex)

    print('For dfs by recursion:')
    print(dfs_recur(adjacency_dict, start_vertex))

if __name__ == '__main__':
    main()
