from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_queue import Queue


def bfs(graph_dict, start_vertex):
	queue = Queue()
	queue.enqueue(start_vertex)

    visited_set = set()

	while queue:
		path = queue.dequeue()
		vertex = path[-1]
		yield vertex, path
		for neighbor in graph_dict[vertex] - visited_set:
			visited_set.add(neighbor)
			queue.enqueue(neighbor)


def traverse(graph_dict, start_vertex, end_vertex):
	for vertex, path in breadth_first_search(graph_dict, start_vertex):
		if vertex == end_vertex:
			print(' -> '.join(path))


def main():
	# Small word ladder graph.
	graph_dict = {
	    'fool': {'cool', 'pool', 'foil', 'foul'},
	    'foul': {'fool', 'foil'},
	    'foil': {'fool', 'foul', 'fail'},
	    'cool': {'fool', 'cool'},
	    'fail': {'foil', 'fall'},
	    'fall': {'fail', 'pall'},
	    'pool': {'fool', 'cool', 'poll'},
	    'poll': {'pool', 'pail'},
	    'pall': {'fall', 'pale', 'poll'},
	    'pole': {'poll', 'pope', 'pale'},
	    'pale': {'pall', 'pole', 'sale', 'page'},
	    'sale': {'pale', 'sage'},
	    'page': {'pale', 'sage'},
	    'sage': {'sale', 'page'} 
	}

    start_vertex = 'fool'
    end_vertex = 'sage'
	traverse(graph_dict, start_vertex, end_vertex)

if __name__ == '__main__':
	main()
