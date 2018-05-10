from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def sort_edges_by_weight(w_graph_d):
	pass


def make_set(v, previous_d, rank_d):
	previous_d[v] = v
	rank_d[v] = 0
	return previous_d, rank_d


def link(v, u, previous_d, rank_d):
	"""Link method.

	Changes the parent pointer of one of roots, say v,
	and makes it point to y. Return the root of composit tree u.
	"""
	pass


def find(v, previous_d):
	"""Find method. 

	Make each vertices point directly to the root.
	"""
	pass


def union(v, u, previous_d, rank_d):
	"""Union by rank method.
    
    Make the shorter tree nodes to the root of the longer.
	"""
	pass


def kruskal(w_graph_d):
	"""Kruskal's algorithm for minimum spanning tree 
	in undirected weighted graph.

    Time complexity for graph G(V, E): 
        O(|E|+|V|+|E|log(|V|)) 
        = O(|E|log(|V|^2)) 
        = O(|E|log(|V|)).
	"""
	mst_set = set()
	sorted_edges_d = sort_edges_by_weight(w_graph_d)

	previous_d = {} 
	rank_d = {}

	for v in w_graph_d.keys():
		previous_d, rank_d = make_set(v, previous_d, rank_d)

	for (v, u) in sorted_edges_d.keys():
		find_v, previous_d = find(v, previous_d)
		find_u, previous_d = find(u, previous_d)
		if find_v != find_u:
			mst_set.add((v, u))
			u, previous_d, rank_d = union(v, u, previous_d, rank_d)

	return mst_set, previous_d, rank_d


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

    print('Kruskal\'s minimum spanning tree:')
    pass


if __name__ == '__main__':
	main()
