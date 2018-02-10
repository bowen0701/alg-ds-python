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

    def min_heapify(self, i):
    	l = left(i)
    	r = right(i)
    	if l <= self.heap_size and self.heap_ls[l] < self.heap_ls[i]:
    		minimum = l
    	if r <= self.heap_size and self.heap_ls[r] < self.heap_ls[minimum]:
    		minimum = r
    	if minimum != i:
    		self.heap_ls[i], self.heap_ls[minimum] = (
    			self.heap_ls[minimum], self.heap_ls[i])
    		min_heapify(self, minimum)


def main():
	pass


if __name__ == '__main__':
	main()
