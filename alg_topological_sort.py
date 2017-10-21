def topological_sort_recur(adjacency_dict, start_vertex,
	                       visited_set, finish_ls):
	"""Topological Sorting by Recursion."""
	visited_set.add(start_vertex)
	for neighbor_vertex in adjacency_dict[start_vertex]:
		if neighbor_vertex not in visited_set:
			topological_sort_recur(
				adjacency_dict, neighbor_vertex,
	            visited_set, finish_ls)
	finish_ls.insert(0, start_vertex)
	print(finish_ls)


def topological_sort(adjacency_dict):
	"""Topological Sorting for Directed Acyclic Graph (DAG)."""
	visited_set = set()
	finish_ls = []
	for vertex in adjacency_dict:
		if vertex not in visited_set:
			topological_sort_recur(
				adjacency_dict, vertex,
	            visited_set, finish_ls)
	print(finish_ls)


def main():
	# DAG.
	dag_adjacency_dict = {
	    'A': {'D'},
	    'B': {'D'},
	    'C': {'D'},
	    'D': {'G', 'E'},
	    'E': {'J'},
	    'F': {'G'},
	    'G': {'I'},
	    'I': {'J'},
	    'J': {}
	}

	topological_sort(dag_adjacency_dict)

if __name__ == '__main__':
	main()
