from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_binary_heap_tuple import BinaryHeap

def dijkstra(weighted_graph_d, start_vertex):
    shortest_path_d = {
        vertex: float('inf') for vertex in weighted_graph_d
    }
    shortest_path_d[start_vertex] = 0

    distance_vertex_ls = [
        (distance, vertex) for vertex, distance 
        in shortest_path_d.items()]
    
    bh = BinaryHeap()
    bh.build_heap(distance_vertex_ls)
    print(bh.heap_ls)
    # TODO: Continue Dijkstra's algorithm.


def main():
    weighted_graph_d = {
        'u': {'v': 2, 'w': 5, 'x': 1},
        'v': {'u': 2, 'w': 3, 'x': 2},
        'w': {'u': 5, 'v': 3, 'x': 3, 'y': 1, 'z': 5},
        'x': {'u': 1, 'v': 2, 'w': 3, 'y': 1},
        'y': {'w': 1, 'x': 1, 'z': 1},
        'z': {'w': 5, 'y': 1}
    }

    dijkstra(weighted_graph_d, 'u')

if __name__ == '__main__':
    main()
