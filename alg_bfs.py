from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_queue import Queue


def breadth_first_search(graph_dict, start_vertex):
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



def main():
	pass

if __name__ == '__main__':
	main()
