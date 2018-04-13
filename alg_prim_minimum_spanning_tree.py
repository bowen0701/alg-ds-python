from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from ds_min_priority_queue_tuple import MinPriorityQueue


def prim():
	"""Prim's algorithm for minimum spanning tree in weighted graph.

	Time complexity for graph G(V, E): (|V|+|E|)log(|V|).
	"""
	pass


def main():
	w_graph_d = {
	    'a': {'b': 1, 'd': 4, 'e': 3},
	    'b': {'a': 1, 'd': 4, 'e': 2},
	    'c': {'e': 4, 'f': 5},
	    'd': {'a': 4, 'b': 4, 'e': 4},
	    'e': {'a': 3, 'b': 2, 'c': 4, 'd': 4, 'f': 7},
	    'f': {'c': 5, 'e': 7}
	}
	start_vertex = 'a'
    print('w_graph_d:\n{}'.format(w_graph_d))
    print('Prim minimum spanning tree from {}:'.format(start_vertex))
    pass


if __name__ == '__main__':
	main()
