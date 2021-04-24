from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1


class MaxHeap(object):
    """Max Heap data structure.

    Max-heap property: A[i] >= A[child(i)].

    Application: 
      - Heapsort algorithm
      - Max Priority Queue data structure
      - Job scheduler (by prirority)
    """
    def __init__(self):
        # Add extra before real root for left/right node computation.
        self.A = [0]
        self.size = 0

    def show(self):
        print(self.A[1:])

    def get_max(self):
        return self.A[1]

    def heapify(self, i):
        """Max heapify in a top-down manner by recursion.

        Time complexity: O(log(i)).
        Space complexity: O(1).
        """
        l = left(i)
        r = right(i)

        # Get max index from node i and its two child nodes.
        if l <= self.size and self.A[l] > self.A[i]:
            max_i = l
        else:
            max_i = i
        if r <= self.size and self.A[r] > self.A[max_i]:
            max_i = r

        # If node i is not max, swap node i and node max_i.
        if max_i != i:
            self.A[i], self.A[max_i] = self.A[max_i], self.A[i]
            self.heapify(max_i)

    def build(self, A):
        """Build max heap bottom-up from unordered numbers.

        Time cmplexity: O(n) (tight bound, although looks like nlog(n)).
        Space complexity: O(1).
        """
        self.A.extend(A)
        self.size = len(A)

        # Reversely start from level-1 nodes from leaves up to level-log(n) (= 1) node.
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)

    def extract_max(self):
        """Extract max.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        if self.size < 1:
            raise ValueError('Heap underflow.')

        maximum = self.A[1]

        # Pop the last node and insert to max, then perform heapify. 
        last = self.A.pop()
        self.size -= 1

        if self.size < 1:
            pass
        else:
            self.A[1] = last
            self.heapify(1)

        return maximum

    def increase_key(self, i, key):
        """Increase key.

        Time complexity: O(log(n)).
        Space complexity: O(1).
        """
        if self.A[i] > key:
            raise ValueError(f"new key {key} is smaller than current key {i}")

        # For node i, check if it's bigger than parent. If yes, swap them.
        self.A[i] = key
        while i > 1 and self.A[parent(i)] < self.A[i]:
            self.A[i], self.A[parent(i)] = self.A[parent(i)], self.A[i]
            i = parent(i)

    def insert(self, key):
        """Insert key.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        # Add to the tree a new leaf whose key is -inf.
        self.size += 1
        self.A.append(-float('inf'))
        self.increase_key(self.size, key)


def main():
    print('Build max heap from unordered list:')
    max_heap = MaxHeap()
    max_heap.build([1, 3, 5, 7, 9, 11])
    max_heap.show()

    print('Max Heap by inserting 1, 3, 5, 7:')
    max_heap = MaxHeap()
    max_heap.insert(1)
    max_heap.insert(3)
    max_heap.insert(5)
    max_heap.insert(7)
    max_heap.show() 

    print('Get max:')
    print(max_heap.get_max())

    print('Extract max:')
    maximum = max_heap.extract_max()
    print(maximum)
    print('The remaining:')
    max_heap.show()


if __name__ == '__main__':
    main()
