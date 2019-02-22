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


class MaxHeapAttribute(object):
    """Max Heap with Attribute implementation of Priority Queue.

    Max-heap property: A[parent(i)][0] >= A[i][0], i = left, right.
    """
    def __init__(self):
        self.A = [[0, 0]]
        self.size = 0

    def show(self):
        print(self.A)

    def get_max(self):
        return self.A[1]

    def heapify_up(self, i):
        """Max heapify up.

        Complexity: O(log(n)).
        """
        while i > 1 and self.A[parent(i)][0] < self.A[i][0]:
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def add(self, new_key_item):
        key, item = new_key_item
        self.size += 1
        self.A.append([key, item])
        self.heapify_up(self.size)

    def heapify_down(self, i):
        """Max heapify down.

        Complexity: O(log(n)).
        """ 
        l = left(i)
        r = right(i)
        if l <= self.size and self.A[l][0] > self.A[i][0]:
            max_i = l
        else:
            max_i = i
        if r <= self.size and self.A[r][0] > self.A[max_i][0]:
            max_i = r
        if max_i != i:
            # Swap node i and node max_i.
            self.A[i], self.A[max_i] = self.A[max_i], self.A[i]
            self.heapify_down(max_i)

    def build(self, arr):
        """Build max heap from unordered array.

        Start from level-1 nodes from leaves back to level-log(n) node.
        Specifically, node (n/2), node (n/2 - 1), ..., node 1, where
        n is the number of nodes including the root node. 

        Complexity: O(n*log(n)) via simple analysis. Actually O(n).
        """
        self.A.extend(arr)
        self.size = len(arr)
        for i in reversed(range(1, (self.size + 1) // 2 + 1)):
            self.heapify_down(i)

    def extract_max(self):
        if self.size < 1:
            raise ValueError('Heap underflow.')
        maximum = self.A[1]
        last = self.A.pop()
        self.size -= 1
        if self.size < 1:
            # The last element is maximum.
            pass
        else:
            self.A[1] = last
        self.heapify_down(1)
        return maximum


def main():
    print('Max heap of vertices by inserting [1, a], [3, c], [5, b], [7, e]:')
    max_pq = MaxHeapAttribute()
    max_pq.add([1, 'a'])
    max_pq.add([3, 'c'])
    max_pq.add([5, 'b'])
    max_pq.add([7, 'e'])
    max_pq.show()

    print('Build heap of vertices from unordered list')
    print('[[1, a], [3, c], [5, b], [7, e]]:')
    max_pq = MaxHeapAttribute()
    max_pq.build([[1, 'a'], [3, 'c'], [5, 'b'], [7, 'e']])
    max_pq.show()

    print('Get max:')
    print(max_pq.get_max())

    print('Extract max:')
    _max = max_pq.extract_max()
    print(_max)
    print('The remaining:')
    max_pq.show()


if __name__ == '__main__':
    main()
