from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


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

    def heap_show(self):
    	print(self.heap_ls)

    def heap_min(self):
    	return self.heap_ls[1]

    def heap_extract_min(self):
    	if self.heap_size < 1:
    		raise ValueError('Heap underflow.')
    	minimum = self.heap_ls[1]
    	self.heap_ls[1] = self.heap_ls[self.heap_size]
    	min_heapify(self, 1)
    	return minimum

    def heap_decrease_key(self, i, key):
    	if key > self.heap_ls[i]:
    		raise ValueError('New key is larger than current key.')
    	self.heap_ls[i] = key
    	while i > 1 and self.heap_ls[parent(i)] > self.heap_ls[i]:
    		self.heap_ls[i], self.heap_ls[parent(i)] = (
    			self.heap_ls[parent(i)], self.heap_ls[i])
    		i = parent(i)

    def min_heap_insert(self, key):
    	self.heap_size += 1
    	self.heap_ls[self.heap_size] = np.inf
    	heap_decrease_key(self, self.heap_size, key)


def main():
	pass


if __name__ == '__main__':
	main()
