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

	def add_neighbor(self, new_nb, weight=0):
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
    	self.num_vertices += 1
    	new_vertex = Vertex(key)
    	self.vertex_dict[key] = new_vertex
    	return new_vertex

    def get_vertex(self, key):
    	self.vertex_dict.get(key, None)

    def __contains__(self, key):
    	return key in self.vertex_dict

    def add_edge(self, from_key, to_key, weight=0):
    	if from_key is not in self.vertex_dict:
    		new_vertex = self.add_vertex(from_key)
    	else:
    		pass
    	if to_key is not in self.vertex_dict:
    		new_vertex = self.add_vertex(to_key)
    	else:
    		pass
    	(self.vertex_dict.get(from_key)
    		 .add_neighbor(self.vertex_dict.get(to_key), weight))

    def get_vertices(self):
    	return self.vertex_dict.keys()

    def __iter__(self):
    	return iter(self.vertex_dict.values())


def main():
    pass


if __name__ == '__main__':
    main()
