from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import numpy as np

def bfs(graph_adj_d, start_vertex):
    visit_queue = []
    visit_queue.insert(0, start_vertex)
    distance_d = {v: np.inf for v in graph_adj_d.keys()}
    distance_d[start_vertex] = 0
    while visit_queue:
        v_visit = visit_queue.pop()
        for v_neighbor in graph_adj_d[v_visit]:
            if np.isinf(distance_d[v_neighbor]):
                visit_queue.insert(0, v_neighbor)
                distance_d[v_neighbor] = distance_d[v_visit] + 1
    return distance_d


def main():
    # Small word ladder graph.
    graph_adj_d = {
        'fool': ['cool', 'pool', 'foil', 'foul'],
        'foul': ['fool', 'foil'],
        'foil': ['fool', 'foul', 'fail'],
        'cool': ['fool', 'pool'],
        'fail': ['foil', 'fall'],
        'fall': ['fail', 'pall'],
        'pool': ['fool', 'cool', 'poll'],
        'poll': ['pool', 'pall', 'pole'],
        'pall': ['fall', 'pale', 'poll'],
        'pole': ['poll', 'pope', 'pale'],
        'pope': ['pole'],
        'pale': ['pall', 'pole', 'sale', 'page'],
        'sale': ['pale', 'sage'],
        'page': ['pale', 'sage'],
        'sage': ['sale', 'page'] 
    }
    print('Graph:\n{}'.format(graph_adj_d))

    start_vertex = 'fool'
    print('Start vertex: {}'.format(start_vertex))
    distance_d = bfs(graph_adj_d, start_vertex)
    print('Using BFS with queue, the distance dict is\n{}'
          .format(distance_d))


if __name__ == '__main__':
    main()
