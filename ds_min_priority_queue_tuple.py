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


class MinPriorityQueue(object):
    """Min Priority Queue."""
    def __init__(self):
        self.heap_ls = [(0, 0)]
        self.heap_size = 0

    def show(self):
        print(self.heap_ls)

    def min_heapify(self, i):
        l = left(i)
        r = right(i)
        if l <= self.heap_size and self.heap_ls[l][0] < self.heap_ls[i][0]:
            min_i = l
        else:
            min_i = i
        if r <= self.heap_size and self.heap_ls[r][0] < self.heap_ls[min_i][0]:
            min_i = r
        if min_i != i:
            self.heap_ls[i][1], self.heap_ls[min_i][1] = (
                self.heap_ls[min_i][1], self.heap_ls[i][1])
            self.min_heapify(min_i)

    def find_min(self):
        return self.heap_ls[1]

    def extract_min(self):
        if self.heap_size < 1:
            raise ValueError('Heap underflow.')
        minimum = self.heap_ls[1]
        self.heap_ls[1] = self.heap_ls.pop()
        self.heap_size -= 1
        self.min_heapify(1)
        return minimum

    # TODO.
    def decrease_key(self, i, key):
        if key > self.heap_ls[i]:
            raise ValueError('New key is larger than current key.')
        self.heap_ls[i] = key
        while i > 1 and self.heap_ls[parent(i)] > self.heap_ls[i]:
            self.heap_ls[i], self.heap_ls[parent(i)] = (
                self.heap_ls[parent(i)], self.heap_ls[i])
            i = parent(i)

    def insert(self, key):
        self.heap_size += 1
        self.heap_ls.append(np.inf)
        self.decrease_key(self.heap_size, key)


def main():
    min_pq = MinPriorityQueue()

    # Insert sequentially 5, 7, 3, 1.
    print('Insert 5')
    min_pq.insert(5)
    min_pq.show()

    print('Insert 7')
    min_pq.insert(7)
    min_pq.show()

    print('Insert 3')
    min_pq.insert(3)
    min_pq.show()

    print('Insert 1')
    min_pq.insert(1)
    min_pq.show()

    # Decrease key 7 at position 4 to 2.
    print('Decrease key 7 at position 4 to 2.')
    min_pq.decrease_key(4, 2)
    min_pq.show()


if __name__ == '__main__':
    main()
