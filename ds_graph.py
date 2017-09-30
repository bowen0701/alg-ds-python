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
    	if from_key not in self.vertex_dict:
    		new_vertex = self.add_vertex(from_key)
    	else:
    		pass
    	if to_key not in self.vertex_dict:
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
    g = Graph()
    for k in xrange(6):
    	g.add_vertex(k)
    g.vertex_dict

    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 2, 1)
    g.add_edge(5, 4, 8)

    for k in g:
    	for c in k.get_connections():
    		print('({}, {})'.format(k.get_id(), c.get_id()))


if __name__ == '__main__':
    main()
