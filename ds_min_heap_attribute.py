from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1


class MinHeapAttribute(object):
    """Min Heap with Attribute implmentation of Priority Queue.

    Min-heap property: A[parent(i)][0] <= A[i][0], i = left, right.

    Applications:
      - Dijkstra's Algorithm.
      - Prim's Minimum Spanning Tree Algorithm.
    """
    def __init__(self):
        # Add extra before real root for left/right node computation.
        self.A = [[0, 0]]
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
        while i > 1 and self.A[parent(i)][0] > self.A[i][0]:
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, new_key_item):
        """insert new key to heap.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        # Append new key to the end of the list, then heapify up.
        key, item = new_key_item        
        self.A.append([key, item])
        self.size += 1
        self._heapify_up(self.size)

    def _heapify_down(self, i):
        """Min heapify down by recusion.

        Time complexity: O(log(i)).
        Space complexity: O(1).
        """ 
        l = left(i)
        r = right(i)

        # Get min index from node i and its two child nodes.
        if l <= self.size and self.A[l][0] < self.A[i][0]:
            min_i = l
        else:
            min_i = i
        if r <= self.size and self.A[r][0] < self.A[min_i][0]:
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

        # Pop the last node and insert to max, then perform heapify down. 
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

        Start from level-1 nodes from leaves back to level-long(n) nodes.
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
    print('Min Heap of vertices by inserting [7, a], [5, c], [3, b], [1, e]:')
    min_pq = MinHeapAttribute()
    min_pq.insert([7, 'a'])
    min_pq.insert([5, 'b'])
    min_pq.insert([3, 'c'])
    min_pq.insert([1, 'e'])
    min_pq.show()

    print('Get min key:')
    print(min_pq.get_min())

    print('Extract min key:')
    _min = min_pq.extract_min()
    print('- Min: {}'.format(_min))
    print('- The remaining:')
    min_pq.show()

    print('Build min heap of vertices from unordered list')
    print('[[7, a], [5, c], [3, b], [1, e]]:')
    min_pq = MinHeapAttribute()
    min_pq.build([[7, 'a'], [5, 'c'], [3, 'b'], [1, 'e']])
    min_pq.show()


if __name__ == '__main__':
    main()
