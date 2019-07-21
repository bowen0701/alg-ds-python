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
        # Add extra before real root for left/right node computation.
        self.A = [0]
        self.size = 0

    def show(self):
        print(self.A[1:])

    def get_min(self):
        return self.A[1]

    def _heapify_up(self, i):
        """Min heapify up by iteration.

        Time complexity: O(log(i)).
        Space complexity: O(1).
        """
        # For node i, check if it's smaller than parent. If yes, swap them.
        while i > 1 and self.A[parent(i)] > self.A[i]:
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, new_key):
        """insert new key to heap.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        # Append new key to the end of the list, then heapify up.
        self.A.append(new_key)
        self.size += 1
        self._heapify_up(self.size)

    def _heapify_down(self, i):
        """Min heapify down by recursion.

        Time complexity: O(log(i)).
        Space complexity: O(1).
        """
        l = left(i)
        r = right(i)

        # Get min index from node i and its two child nodes.
        if l <= self.size and self.A[l] < self.A[i]:
            min_i = l
        else:
            min_i = i
        if r <= self.size and self.A[r] < self.A[min_i]:
            min_i = r

        # If node i is not min, swap node i and node min_i.
        if min_i != i:
            self.A[i], self.A[min_i] = self.A[min_i], self.A[i]
            self._heapify_down(min_i)

    def extract_min(self):
        """Extract min.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        if self.size < 1:
            raise ValueError('Heap underflow.')

        minimum = self.A[1]

        # Pop the last node and insert to min, then perform heapify down. 
        last = self.A.pop()
        self.size -= 1

        if self.size < 1:
            # The last element is minimum.
            pass
        else:
            # Insert the last to root, then heapify down.
            self.A[1] = last
            self._heapify_down(1)

        return minimum

    def build(self, arr):
        """Build min heap from unordered array.

        Start from the level-1 nodes from leaves back to level-log(n) node.
        Specifically, node (n/2), node (n/2 - 1), ..., node 1, where
        n is the number of nodes including the root one, heapify down them.

        Time cmplexity: O(n*log(n)) via simple analysis. Actually O(n).
        Space complexity: O(1).
        """
        self.A.extend(arr)
        self.size = len(arr)
        for i in reversed(range(1, (self.size + 1) // 2 + 1)):
            self._heapify_down(i)


def main():
    print('Min heap by inserting 7, 5, 3, 1:')
    min_pq = MinHeap()
    min_pq.insert(7)
    min_pq.insert(5)
    min_pq.insert(3)
    min_pq.insert(1)
    min_pq.show()

    print('Get min key:')
    print(min_pq.get_min())

    print('Extract min key:')
    _min = min_pq.extract_min()
    print('- Min: {}'.format(_min))
    print('- The remaining:')
    min_pq.show()

    print('Build min heap from unordered list [7, 5, 3, 1]:')
    min_pq = MinHeap()
    min_pq.build([7, 5, 3, 1])
    min_pq.show()


if __name__ == '__main__':
    main()
