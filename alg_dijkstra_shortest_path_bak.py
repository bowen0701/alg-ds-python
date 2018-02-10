from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_min_binary_heap_tuple_bak import MinBinaryHeap


def dijkstra(weighted_graph_d, start_vertex):
    shortest_path_d = {
        vertex: float('inf') for vertex in weighted_graph_d
    }
    shortest_path_d[start_vertex] = 0
    
    distance_vertex_ls = [
        (distance, vertex) for vertex, distance 
        in shortest_path_d.items()]

    bh = MinBinaryHeap()
    bh.build_heap(distance_vertex_ls)

    vertex_lookup_d = {vertex: None for vertex in shortest_path_d.keys()}
    vertex_lookup_d[start_vertex] = start_vertex

    while len(bh) > 0:
        current_distance, current_vertex = bh.delete_min()

        for neighbor_vertex, neighbor_distance in weighted_graph_d[current_vertex].items():
            distance = shortest_path_d[current_vertex] + neighbor_distance
            if distance < shortest_path_d[neighbor_vertex]:
                shortest_path_d[neighbor_vertex] = distance
                vertex_lookup_d[neighbor_vertex] = current_vertex
                bh.decrease_key(neighbor_vertex, neighbor_distance)

    return shortest_path_d, vertex_lookup_d


def main():
    weighted_graph_d = {
        'u': {'v': 2, 'w': 5, 'x': 1},
        'v': {'u': 2, 'w': 3, 'x': 2},
        'w': {'u': 5, 'v': 3, 'x': 3, 'y': 1, 'z': 5},
        'x': {'u': 1, 'v': 2, 'w': 3, 'y': 1},
        'y': {'w': 1, 'x': 1, 'z': 1},
        'z': {'w': 5, 'y': 1}
    }
    start_vertex = 'x'
    print('weighted_graph_d: {}'.format(weighted_graph_d))
    print('Dijkstra shortest path from {}:'.format(start_vertex))
    shortest_path_d, vertex_lookup_d = dijkstra(weighted_graph_d, start_vertex)
    print('shortest_path_d: {}'.format(shortest_path_d))
    print('vertex_lookup_d: {}'.format(vertex_lookup_d))


if __name__ == '__main__':
    main()
