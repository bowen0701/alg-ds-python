from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1


class MinHeap(object):
    """Min Heap data structure.

    Min-heap property: A[i] <= A[child(i)].

    Applications:
      - Min Priority Queue data structure
      - Event-driven simulator
      - Dijkstra's algorithm
      - Prim's Minimum Spanning Tree algorithm
    """
    def __init__(self):
        # Add extra before real root for left/right node computation.
        self.A = [0]
        self.size = 0

    def show(self):
        print(self.A[1:])

    def get_min(self):
        return self.A[1]

    def heapify(self, i):
        """Min heapify in a top-down manner by recursion.

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
            self.heapify(min_i)

    def build(self, A):
        """Build min heap bottom-up from unordered numbers.

        Time cmplexity: O(n) (tight bound, although looks like nlog(n)).
        Space complexity: O(1).
        """
        self.A = [0]
        self.A.extend(A)
        self.size = len(A)

        # Reversely start from level-1 nodes from leaves up to level-log(n) (= 1) node.
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)

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
            pass
        else:
            self.A[1] = last
            self.heapify(1)

        return minimum

    def decrease_key(self, i, key):
        """Decrease key.

        Time complexity: O(log(n)).
        Space complexity: O(1).
        """
        if self.A[i] < key:
            raise ValueError(f"new key {key} is larger than current key {i}")

        # For node i, check if it's smaller than parent. If yes, swap them.
        self.A[i] = key
        while i > 1 and self.A[parent(i)] > self.A[i]:
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, key):
        """Insert key to heap.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        # Add to the tree a new leaf whose key is inf.
        self.size += 1
        self.A.append(float('inf'))
        self.decrease_key(self.size, key)


def main():
    print('Build min heap from unordered list:')
    min_heap = MinHeap()
    min_heap.build([1, 3, 5, 7, 9, 11])
    min_heap.show()

    print('Min heap by inserting 7, 5, 3, 1:')
    min_heap = MinHeap()
    min_heap.insert(7)
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.show()

    print('Get min key:')
    print(min_heap.get_min())

    print('Extract max:')
    minimum = min_heap.extract_min()
    print(minimum)
    print('The remaining:')
    min_heap.show()


if __name__ == '__main__':
    main()
