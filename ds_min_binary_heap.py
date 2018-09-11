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
    """Min Binary Heap implmentation of Priority Queue.

    Min-heap property: A[parent(i)] <= A[i].
    """
    def __init__(self):
        self.A = [0]
        self.size = 0

    def show(self):
        print(self.A)

    def find_min(self):
        return self.A[1]

    def min_heapify(self, i):
        """Min heapify operation.

        Complexity: log(n).
        """
        l = left(i)
        r = right(i)
        if l <= self.size and self.A[l] < self.A[i]:
            min_i = l
        else:
            min_i = i
        if r <= self.size and self.A[r] < self.A[min_i]:
            min_i = r
        if min_i != i:
            self.A[i], self.A[min_i] = self.A[min_i], self.A[i]
            self.min_heapify(min_i)

    def extract_min(self):
        if self.size < 1:
            raise ValueError('Heap underflow.')
        minimum = self.A[1]
        last = self.A.pop()
        self.size -= 1
        if self.size < 1:
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
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, new_key):
        self.A.append(np.inf)
        self.size += 1
        self.decrease_key(self.size, new_key)


def main():
    min_pq = MinBinaryHeap()

    print('Binary heap with 5, 7, 3, 1:')
    min_pq.insert(5)
    min_pq.insert(7)
    min_pq.insert(3)
    min_pq.insert(1)
    min_pq.show()

    # print('Decrease key 7 at position 4 to 2.')
    # min_pq.decrease_key(4, 2)
    # min_pq.show()

    # print('Find min key:')
    # print(min_pq.find_min())

    print('Extract min key:')
    _min = min_pq.extract_min()
    print('- Min: {}'.format(_min))
    print('- The remaining:')
    min_pq.show()


if __name__ == '__main__':
    main()
