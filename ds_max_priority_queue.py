from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1


class MaxPriorityQueue(object):
	"""Max Priority Queue."""
	def __init__(self):
		self.heap_ls = [0]
		self.heap_size = 0

    def heap_show(self):
		print(self.heap_ls)

	def max_heapify(self, i):
		l = left(i)
		r = right(r)

		if l <= self.heap_size and self.heap_ls[l] > self.heap_ls[i]:
			max_i = l
		if r <= self.heap_size and self.heap_ls[r] > self.heap_ls[max_i]:
			max_i = r
		if max_i != i:
			self.heap_ls[i], self.heap_ls[max_i] = (
				self.heap_ls[max_i], self.heap_ls[i])
			self.max_heapify(max_i)

    def heap_max(self):
        return self.heap_ls[1]

    def heap_extract_max(self):
        if self.heap_size < 1:
            raise ValueError('Heap underflow.')
        maximum = self.heap_ls[1]
        self.heap_ls[1] = self.heap_ls[self.heap_size]
        self.max_heapify(1)
        return maximum

    def heap_increase_key(self, i, key):
        if key < self.heap_ls[i]:
            raise ValueError('New key is smaller than current key.')
        self.heap_ls[i] = key
        while i > 1 and self.heap_ls[parent(i)] < self.heap_ls[i]:
            self.heap_ls[i], self.heap_ls[parent(i)] = (
                self.heap_ls[parent(i)], self.heap_ls[i])
            i = parent(i)


def main():
	pass


if __name__ == '__main__':
	main()
