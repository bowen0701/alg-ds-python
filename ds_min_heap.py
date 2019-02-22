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


class MinHeap(object):
    """Min Heap implmentation of Priority Queue.

    Min-heap property: A[parent(i)] <= A[i], i = left, right.
    """
    def __init__(self):
        self.A = [0]
        self.heap_size = 0

    def show(self):
        print(self.A)

    def find_min(self):
        return self.A[1]

    def min_heapify(self, i):
        """Min heapify.

        Complexity: O(log(n)).
        """
        l = left(i)
        r = right(i)
        if l <= self.heap_size and self.A[l] < self.A[i]:
            min_i = l
        else:
            min_i = i
        if r <= self.heap_size and self.A[r] < self.A[min_i]:
            min_i = r
        if min_i != i:
            # Swap node i and node min_i.
            self.A[i], self.A[min_i] = self.A[min_i], self.A[i]
            self.min_heapify(min_i)

    def build_min_heap(self, arr):
        """Build min heap from unordered array.

        Start from the level-1 nodes from leaves back to level-log(n) node.
        Specifically, node (n/2), node (n/2 - 1), ..., node 1, where
        n is the number of nodes including the root one.

        Complexity: O(n*log(n)) via simple analysis. Actually O(n).
        """
        self.A.extend(arr)
        self.heap_size = len(arr)
        for i in reversed(range(1, (self.heap_size + 1) // 2 + 1)):
            self.min_heapify(i)

    def extract_min(self):
        if self.heap_size < 1:
            raise ValueError('Heap underflow.')
        minimum = self.A[1]
        last = self.A.pop()
        self.heap_size -= 1
        if self.heap_size < 1:
            # The last element is minimum.
            pass
        else:
            self.A[1] = last
            self.min_heapify(1)
        return minimum

    def decrease_key(self, i, key):
        if key > self.A[i]:
            raise ValueError('New key is larger than current key.')
        self.A[i] = key
        while i > 1 and self.A[parent(i)] > self.A[i]:
            # Swap node i and node parent(i).
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, new_key):
        self.A.append(np.inf)
        self.heap_size += 1
        self.decrease_key(self.heap_size, new_key)


def main():
    print('Min heap by inserting 3, 7, 5, 1:')
    min_pq = MinHeap()
    min_pq.insert(3)
    min_pq.insert(7)
    min_pq.insert(5)
    min_pq.insert(1)
    min_pq.show()

    print('Build min heap from unordered list [3, 7, 5, 1]:')
    min_pq = MinHeap()
    min_pq.build_min_heap([3, 7, 5, 1])
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
