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
        self.heap_ls = [[0, 0]]
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

    def decrease_key(self, i, key):
        if key > self.heap_ls[i][0]:
            raise ValueError('New key is larger than current key.')
        self.heap_ls[i][0] = key
        while i > 1 and self.heap_ls[parent(i)][0] > self.heap_ls[i][0]:
            self.heap_ls[i][1], self.heap_ls[parent(i)][1] = (
                self.heap_ls[parent(i)][1], self.heap_ls[i][1])
            i = parent(i)

    def insert(self, new_node):
        key, item = new_node
        self.heap_size += 1
        self.heap_ls.append((np.inf, item))
        self.decrease_key(self.heap_size, key)


def main():
    print('Binary heap tuple with [1, a], [3, c]', 
          '[4, b], [5, e], [2, d]:')
    min_pq = MinPriorityQueue()
    min_pq.insert([1, 'a'])
    min_pq.insert([3, 'c'])
    min_pq.insert([4, 'b'])
    min_pq.insert([5, 'e'])
    min_pq.insert([2, 'd'])
    min_pq.show()

    print('Decrease key 5 at position 4 to 2.')
    min_pq.decrease_key(4, 2)
    min_pq.show()


if __name__ == '__main__':
    main()
