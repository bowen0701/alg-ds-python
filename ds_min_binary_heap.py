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


class MinBinaryHeap(object):
    """Min Binary Heap implementation for Priority Queue."""
    def __init__(self):
        self.heap_ls = [0]
        self.heap_size = 0

    def show(self):
        print(self.heap_ls)

    def min_heapify(self, i):
        l = left(i)
        r = right(i)
        if l <= self.heap_size and self.heap_ls[l] < self.heap_ls[i]:
            min_i = l
        else:
            min_i = i
        if r <= self.heap_size and self.heap_ls[r] < self.heap_ls[min_i]:
            min_i = r
        if min_i != i:
            self.heap_ls[i], self.heap_ls[min_i] = (
                self.heap_ls[min_i], self.heap_ls[i])
            self.min_heapify(min_i)

    def find_min(self):
        return self.heap_ls[1]

    def extract_min(self):
        if self.heap_size < 1:
            raise ValueError('Heap underflow.')
        minimum = self.heap_ls[1]
        last = self.heap_ls.pop()
        self.heap_size -= 1
        if self.heap_size < 1:
            # The last element is minimum.
            pass
        else:
            self.heap_ls[1] = last        
        self.min_heapify(1)
        return minimum

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
    min_pq = MinBinaryHeap()

    print('Insert sequentially 5, 7, 3, 1')
    min_pq.insert(5)
    min_pq.insert(7)
    min_pq.insert(3)
    min_pq.insert(1)
    min_pq.show()

    print('Decrease key 7 at position 4 to 2.')
    min_pq.decrease_key(4, 2)
    min_pq.show()

    print('Find min:')
    print(min_pq.find_min())

    print('Extract min:')
    _min = min_pq.extract_min()
    print(_min)
    print('The remaining:')
    min_pq.show()

if __name__ == '__main__':
    main()
