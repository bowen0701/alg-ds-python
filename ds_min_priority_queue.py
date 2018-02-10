from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class MinPriorityQueue(object):
	"""Min Priority Queue."""
	def __init__(self):
		self.heap_ls = [0]
		self.heap_size = 0

	def parent(i):
		return i // 2

	def left(i):
		return 2 * i

	def right(i):
		return 2 * i + 1


def main():
	pass


if __name__ == '__main__':
	main()
