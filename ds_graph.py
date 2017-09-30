from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Vertex(object):
	"""Vertex class.

    It uses a dict to keep track of the vertices which it's connected.
	"""
	def __init__(self, key):
		self.id = key
		self.connected_to_dict = {}

	def add_neighnor(self, new_nb, weight=0):
		pass

	def __str__(self):
		pass

	def get_connections(self):
		pass

	def get_id(self):
		pass

	def get_weight(self, new_nb):
		pass


class Graph(object):
    """Graph class.

    It contains a dict to map vertex name to vertex objects.
    """
    pass


def main():
    pass


if __name__ == '__main__':
    main()
