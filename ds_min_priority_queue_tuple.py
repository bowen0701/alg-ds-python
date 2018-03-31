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
            self.heap_ls.append(last)
        else:
            self.heap_ls[1] = last
        self.min_heapify(1)
        return minimum

    def decrease_key(self, i, key):
        if key > self.heap_ls[i][0]:
            raise ValueError('New key is larger than current key.')
        self.heap_ls[i][0] = key
        while i > 1 and self.heap_ls[parent(i)][0] > self.heap_ls[i][0]:
            self.heap_ls[i], self.heap_ls[parent(i)] = (
                self.heap_ls[parent(i)], self.heap_ls[i])
            i = parent(i)

    def insert(self, new_node):
        key, item = new_node        
        self.heap_ls.append([np.inf, item])
        self.heap_size += 1
        self.decrease_key(self.heap_size, key)


def main():
    min_pq = MinPriorityQueue()

    print('Binary heap tuple with [5, a], [7, c], [3, b], [1, e]:')
    min_pq.insert([5, 'a'])
    min_pq.insert([7, 'c'])
    min_pq.insert([3, 'b'])
    min_pq.insert([1, 'd'])
    min_pq.show()

    print('Decrease key 7 at position 4 to 2.')
    min_pq.decrease_key(4, 2)
    min_pq.show()

    print('Find min key:')
    print(min_pq.find_min())

    print('Extract min key:')
    _min = min_pq.extract_min()
    print('- Min: {}'.format(_min))
    print('- The remaining:')
    min_pq.show()


if __name__ == '__main__':
    main()
