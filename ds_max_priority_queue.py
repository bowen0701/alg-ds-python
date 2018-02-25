from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


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

    def show(self):
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

    def find_max(self):
        return self.heap_ls[1]

    def extract_max(self):
        if self.heap_size < 1:
            raise ValueError('Heap underflow.')
        maximum = self.heap_ls[1]
        self.heap_ls[1] = self.heap_ls[self.heap_size]
        self.max_heapify(1)
        return maximum

    def increase_key(self, i, key):
        if key < self.heap_ls[i]:
            raise ValueError('New key is smaller than current key.')
        self.heap_ls[i] = key
        while i > 1 and self.heap_ls[parent(i)] < self.heap_ls[i]:
            self.heap_ls[i], self.heap_ls[parent(i)] = (
                self.heap_ls[parent(i)], self.heap_ls[i])
            i = parent(i)

    def insert(self, key):
        self.heap_size += 1
        self.heap_ls.append(-np.inf)
        self.increase_key(self.heap_size, key)


def main():
    max_pq = MaxPriorityQueue()

    # Insert sequentially [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    print('Insert 16')
    max_pq.insert(16)
    max_pq.show()

    print('Insert 14')
    max_pq.insert(14)
    max_pq.show()

    print('Insert 10')
    max_pq.insert(10)
    max_pq.show()

    print('Insert 8')
    max_pq.insert(8)
    max_pq.show()

    print('Insert 7')
    max_pq.insert(7)
    max_pq.show()

    print('Insert 9')
    max_pq.insert(9)
    max_pq.show()

    print('Insert 3')
    max_pq.insert(3)
    max_pq.show()

    print('Insert 2')
    max_pq.insert(2)
    max_pq.show()

    print('Insert 4')
    max_pq.insert(4)
    max_pq.show()

    print('Insert 1')
    max_pq.insert(1)
    max_pq.show()

    # Increase key 4 at position 9 to 15.
    print('Increase key 4 at position 9 to 15.')
    max_pq.increase_key(9, 15)
    max_pq.show()


if __name__ == '__main__':
    main()
