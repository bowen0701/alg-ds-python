from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def _previsit():
    pass


def _postvisit():
    pass


def dfs():
    pass


def _transpose_graph():
    pass


def _decrease_postvisit_vertex():
    pass


def strongly_connected_components():
    """Strongly connected components for graph.

    Procedure:
      - Call (Depth First Search) DFS on graph G to 
        compute finish times for each vertex.
      - Compute the transpose graph G^T of graph G.
      - Call DFS on G^T, but in the main loop of DFS,
        feed the vertex in the decreasing order of postvisit times.
      - Outpu the vertices of each tree in the DFS forest as
        separate strongly connected components.
    """
    pass


def main():
    # 3 strongly connected graphs: {A, B, D, E, G}, {C}, {F, H, I}.
    adj_dict = {
        'A': ['B'],
        'B': ['C', 'E'],
        'C': ['C', 'F'],
        'D': ['B', 'G'],
        'E': ['A', 'D'],
        'F': ['H'],
        'G': ['E'],
        'H': ['I'],
        'I': ['F']
    }

    strongly_connected_components(adj_dict)

if __name__ == '__main__':
    main()
