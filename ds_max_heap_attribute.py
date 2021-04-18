from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1


class MaxHeapAttribute(object):
    """Max heap with attribute implementation of Priority Queue.

    Max-heap property: A[i][0] >= A[child(i)][0].
    """
    def __init__(self):
        # Add extra before real root for left/right node computation.
        self.A = [[0, 0]]
        self.size = 0

    def show(self):
        print(self.A[1:])

    def get_max(self):
        return self.A[1]

    def _heapify_up(self, i):
        """Max heapify up by iteration.

        Time complexity: O(log(i)).
        Space complexity: O(1).
        """
        # For node i, check if it's bigger than parent. If yes, swap them.
        while i > 1 and self.A[parent(i)][0] < self.A[i][0]:
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, new_key_item):
        """insert new key to heap.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        # Append new key to the end of the list, then heapify up.
        key, item = new_key_item
        self.size += 1
        self.A.append([key, item])
        self._heapify_up(self.size)

    def _heapify_down(self, i):
        """Max heapify down by recursion.

        Time complexity: O(log(i)).
        Space complexity: O(1).
        """ 
        l = left(i)
        r = right(i)

        # Get max index from node i and its two child nodes.
        if l <= self.size and self.A[l][0] > self.A[i][0]:
            max_i = l
        else:
            max_i = i
        if r <= self.size and self.A[r][0] > self.A[max_i][0]:
            max_i = r

        # If node i is not max, swap node i and node max_i.
        if max_i != i:
            self.A[i], self.A[max_i] = self.A[max_i], self.A[i]
            self._heapify_down(max_i)

    def extract_max(self):
        """Extract max.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        if self.size < 1:
            raise ValueError('Heap underflow.')

        maximum = self.A[1]

        # Pop the last node and insert to max, then perform heapify down. 
        last = self.A.pop()
        self.size -= 1

        if self.size < 1:
            # The last element is maximum.
            pass
        else:
            # Insert the last to root, then heapify down.
            self.A[1] = last
            self._heapify_down(1)

        return maximum

    def build(self, arr):
        """Build max heap from unordered array.

        Start from level-1 nodes from leaves back to level-log(n) node.
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
    print('Max heap of vertices by inserting [1, a], [3, c], [5, b], [7, e]:')
    max_pq = MaxHeapAttribute()
    max_pq.insert([1, 'a'])
    max_pq.insert([3, 'c'])
    max_pq.insert([5, 'b'])
    max_pq.insert([7, 'e'])
    max_pq.show()

    print('Get max:')
    print(max_pq.get_max())

    print('Extract max:')
    _max = max_pq.extract_max()
    print(_max)
    print('The remaining:')
    max_pq.show()

    print('Build heap of vertices from unordered list')
    print('[[1, a], [3, c], [5, b], [7, e]]:')
    max_pq = MaxHeapAttribute()
    max_pq.build([[1, 'a'], [3, 'c'], [5, 'b'], [7, 'e']])
    max_pq.show()


if __name__ == '__main__':
    main()
