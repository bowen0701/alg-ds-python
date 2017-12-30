from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def strongly_connected_components():
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
