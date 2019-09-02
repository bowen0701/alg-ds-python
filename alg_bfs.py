from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def bfs(graph_adj_d, v_start):
    """Breadth first search (BFS) algorithm in graph G(V, E) 
    with single source by iteration using queue.

    Note: 
    - There is no intuitive way to combine BFS & recursion,
      since BFS goes level by level.
    - This BFS algorithm can find Shortes Reach Problem
      in "un-weighted" graph.

    Time complexity: O(|V|+|E|).
    Space complexity: O(|V|).
    """
    # Create distance dict.
    distance_d = {v: float('inf') for v in graph_adj_d}
    distance_d[v_start] = 0

    # Apply BFS with queue for shortest distance.
    queue = [v_start]
    
    while queue:
        v_visit = queue.pop()
        for v_neighbor in graph_adj_d[v_visit]:
            # If v_neighbor is not visited.
            if distance_d[v_neighbor] == float('inf'):
                queue.insert(0, v_neighbor)
                distance_d[v_neighbor] = distance_d[v_visit] + 1
    return distance_d


def main():
    # Undirected graph by adjacency list.
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

    v_start = 'A'
    print('Start vertex: {}'.format(v_start))
    distance_d = bfs(graph_adj_d, v_start)
    print('BFS with distances:\n{}'
          .format(sorted(distance_d.items(), key=lambda x: x[1])))


if __name__ == '__main__':
    main()
