from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def dfs_recur(adj_dict, start_vertex, visited_set, finish_ls):
	visited_set.add(start_vertex)
	for neighbor_vertex in adj_dict[start_vertex]:
		if neighbor_vertex not in visited_set:
			dfs_recur(adj_dict, neighbor_vertex, visited_set, finish_ls)
	finish_ls.append(start_vertex)

def traverse_dfs_recur(adj_dict):
	visited_set = set()
	finish_ls = []
	for vertex in adj_dict:
		if vertex not in visited_set:
			dfs_recur(adj_dict, vertex, visited_set, finish_ls)
	return finish_ls

def transpose_graph(adj_dict):
	tr_adj_dict = {}

	for vertex in adj_dict:
		tr_adj_dict[vertex] = set()

    for vertex in adj_dict:
    	for neighbor_vertex in adj_dict[vertex]:
    		tr_adj_dict[neighbor_vertex].add(vertex)

    return tr_adj_dict

def strongly_connected_graph():
    """Find strongly connected graphs by Kosaraju's Algorithm."""
    finish_ls = traverse_dfs_recur(adj_dict)
    rev_finish_ls = list(reversed(finish_ls))


def main():
	# 3 strongly connected graphs: {A, B, D, E, G}, {C}, {F, H, I}.
    adj_dict = {
        'A': {'B'},
        'B': {'C', 'E'},
        'C': {'C', 'F'},
        'D': {'B', 'G'},
        'E': {'A', 'D'},
        'F': {'H'},
        'G': {'E'},
        'H': {'I'},
        'I': {'F'}
    }

    finish_ls = traverse_dfs_recur(adj_dict)
    print('finish_ls: {}'.format(finish_ls))

    rev_finish_ls = list(reversed(finish_ls))
    print('rev_finish_ls: {}'.format(rev_finish_ls))

if __name__ == '__main__':
    main()
