from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

from ds_min_priority_queue_tuple import MinPriorityQueue


def prim(w_graph_d):
	"""Prim's algorithm for minimum spanning tree in weighted graph.

	Time complexity for graph G(V, E): (|V|+|E|)log(|V|).
	"""
	min_pq = MinPriorityQueue()

	key_d = {v: np.inf for v in w_graph_d.keys()}
	previous_d = {v: None for v in w_graph_d.keys()}
	visited_d = {v: False for v in w_graph_d.keys()}

	# Pick an arbitrary vertex as start.
	s = w_graph_d.keys()[0]
	visited_d[s] = True
	key_d[s] = 0
	min_pq.insert([key_d[s], s])
    
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
    print('w_graph_d:\n{}'.format(w_graph_d))
    print('Prim minimum spanning tree')
    pass


if __name__ == '__main__':
	main()
