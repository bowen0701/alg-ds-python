from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_queue import Queue


def bfs(graph_dict, start_vertex):
    """Breadth First Search algorith."""
    ls_queue = Queue()
    ls_queue.enqueue([start_vertex])
    print('ls_queue: {}'.format(ls_queue.show()))
    
    # Record visited vertices.
    visited_set = set([start_vertex])

    while ls_queue.size() > 0:
        path_ls = ls_queue.dequeue()
        # Take the lastest vertex as the new starting one.
        vertex = path_ls[-1]
        print('path_ls: {}'.format(path_ls))
        print('vertex: {}'.format(vertex))
        yield vertex, path_ls
        for neighbor_vertex in graph_dict[vertex] - visited_set:
            print('neighbor_vertex: {}'.format(neighbor_vertex))
            visited_set.add(neighbor_vertex)
            ls_queue.enqueue(path_ls + [neighbor_vertex])
            print('visited_set: {}'.format(visited_set))
            print('ls_queue: {}'.format(ls_queue.show()))


def traverse_bfs(graph_dict, start_vertex, end_vertex):
    """Traverse the breadth first search path.

    Take the end_vertex's path from generator of vertex and path_ls. 
    """
    for vertex, path_ls in bfs(graph_dict, start_vertex):
        if vertex == end_vertex:
            print(' -> '.join(path_ls))


def main():
    # Small word ladder graph.
    graph_dict = {
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
    traverse_bfs(graph_dict, start_vertex, end_vertex)

    print('===')
    start_vertex = 'fool'
    end_vertex = 'pope'
    traverse_bfs(graph_dict, start_vertex, end_vertex)

    print('===')
    start_vertex = 'foul'
    end_vertex = 'sage'
    traverse_bfs(graph_dict, start_vertex, end_vertex)

if __name__ == '__main__':
    main()
