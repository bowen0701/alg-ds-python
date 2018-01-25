from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def _dfs_stack_explore():
    pass

def dfs_stack():
    """Depth first search by iteration algorithm using stack."""
    pass


def main():
	# Connected graph by adjacency dictionary.
    graph_adj_d = {
        'A': ['B', 'D'],
        'B': ['C', 'D'],
        'C': [],
        'D': ['E'],
        'E': ['B', 'F'],
        'F': ['C'],
    }
    print('Graph:\n{}'.format(graph_adj_d))


if __name__ == '__main__':
	main()
