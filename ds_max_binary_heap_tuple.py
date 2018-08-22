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
        self.heap_ls = [[0, 0]]
        self.heap_size = 0

    def show(self):
        print(self.heap_ls)

    def max_heapify(self, i):
        l = left(i)
        r = right(i)
        if l <= self.heap_size and self.heap_ls[l][0] > self.heap_ls[i][0]:
            max_i = l
        else:
            max_i = i
        if r <= self.heap_size and self.heap_ls[r][0] > self.heap_ls[max_i][0]:
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
        last = self.heap_ls.pop()
        self.heap_size -= 1
        if self.heap_size < 1:
            # The last element is maximum.
            pass
        else:
            self.heap_ls[1] = last
        self.max_heapify(1)
        return maximum

    def increase_key(self, i, key):
        if key < self.heap_ls[i][0]:
            raise ValueError('New key is smaller than current key.')
        self.heap_ls[i][0] = key
        while i > 1 and self.heap_ls[parent(i)][0] < self.heap_ls[i][0]:
            self.heap_ls[i], self.heap_ls[parent(i)] = (
                self.heap_ls[parent(i)], self.heap_ls[i])
            i = parent(i)

    def insert(self, new_mode):
        key, item = new_mode
        self.heap_size += 1
        self.heap_ls.append([-np.inf, item])
        self.increase_key(self.heap_size, key)


def main():
    max_pq = MaxPriorityQueue()

    print('Binary heap tuple with [5, a], [7, c], [3, b], [1, e]:')
    max_pq.insert([5, 'a'])
    max_pq.insert([7, 'c'])
    max_pq.insert([3, 'b'])
    max_pq.insert([1, 'd'])
    max_pq.show()

    print('Increase key 1 at position 4 to 6.')
    max_pq.increase_key(4, 6)
    max_pq.show()

    print('Find max:')
    print(max_pq.find_max())

    print('Extract max:')
    _max = max_pq.extract_max()
    print(_max)
    print('The remaining:')
    max_pq.show()

if __name__ == '__main__':
    main()
