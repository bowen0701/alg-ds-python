from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Vertex(object):
	"""Vertex class.

    It uses a dict to keep track of the vertices which it's connected.
	"""
	def __init__(self, key):
		self.id = key
		self.connect_dict = {}

	def add_neighnor(self, new_nb, weight=0):
		self.connect_dict[new_nb] = weight

	def __str__(self):
		print_str = (
			'{} connected to {}'
			.format(self.id, [x.id for x in self.connect_dict]))
		return print_str

	def get_connections(self):
		return self.connect_dict.keys()

	def get_id(self):
		return self.id

	def get_weight(self, new_nb):
		return self.connect_dict.get(new_nb, None)


class Graph(object):
    """Graph class.

    It contains a dict to map vertex name to vertex objects.
    """
    def __init__(self):
    	self.vertex_dict = {}
    	self.num_vertices = 0

    def add_vertex(self, key):
    	pass

    def get_vertex(self, key):
    	pass

    def __contains__(self, key):
    	pass

    def add_edge(self, from_key, to_key, cost=0):
    	pass

    def get_vertices(self):
    	pass

    def __iter__(self):
    	pass


def main():
    pass


if __name__ == '__main__':
    main()
