from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_stack import Stack


# def dfs(adjacency_dict, start_vertex):
#     """Depth First Search algorith."""
#     ls_stack = Stack()
#     ls_stack.push([start_vertex])
#     visited_set = set([start_vertex])

#     while ls_stack.size() > 0:
#         path_ls = ls_stack.pop()
#         # Take the lastest vertex as the new starting one.
#         vertex = path_ls[-1]
#         print('path_ls: {}'.format(path_ls))
#         print('vertex: {}'.format(vertex))
#         yield vertex, path_ls
#         for vertex in adjacency_dict[vertex] - set([start_vertex]):
#             visited_set.add(vertex)
#             ls_stack.push([vertex])
#             dfs(adjacency_dict, vertex)

def dfs_recur(adjacency_dict, start_vertex, end_vertex, path_ls=None):
    if path_ls is None:
        path_ls = [start_vertex]
    else:
        path_ls.append(start_vertex)
    print('path_ls: {}'.format(path_ls))

    if start_vertex == end_vertex:
        return path_ls

    for vertex in adjacency_dict[start_vertex]:
        if vertex not in path_ls:
            path_ls = dfs_recur(adjacency_dict, vertex, end_vertex, path_ls=path_ls)

    return path_ls


def main():
    # Small word ladder graph.
    adjacency_dict = {
        'fool': {'cool', 'pool', 'foil', 'foul'},
        'foul': {'fool', 'foil'},
        'foil': {'fool', 'foul', 'fail'},
        'cool': {'fool', 'cool'},
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
    path_ls = dfs_recur(adjacency_dict, start_vertex, end_vertex, path_ls=None)
    print('path_ls: {}'.format(path_ls))
    # traverse_dfs(adjacency_dict, start_vertex, end_vertex)


if __name__ == '__main__':
    main()
