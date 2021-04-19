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
        """Max heapify in a bottom-up manner by recursion.

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
        """Build max heap from unordered nums.

        Start from the level-1 nodes from leaves down to level-log(n) (= 1) node.

        Time cmplexity: O(n) (note: tight bound)
        Space complexity: O(1).
        """
        self.A.extend(A)
        self.size = len(A)
        # for i in reversed(range(1, (self.size + 1) // 2 + 1)):
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)


def main():
    print('Build max heap from unordered list:')
    max_heap = MaxHeap()
    max_heap.build([1, 3, 5, 7, 9, 11])
    max_heap.show()


if __name__ == '__main__':
    main()
