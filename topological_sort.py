def topological_sort_recur():
	"""Topological Sorting by Recursion."""
	pass

def topological_sort():
	"""Topological Sorting for Directed Acyclic Graph (DAG)."""
	pass


def main():
	# DAG.
	adjacency_dict = {
	    '0': {},
	    '1': {},
	    '2': {'3'},
	    '3': {'1'},
	    '4': {'0', '1'},
	    '5': {'0', '2'}
	}

if __name__ == '__main__':
	main()
