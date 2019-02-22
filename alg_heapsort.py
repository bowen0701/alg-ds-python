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
    def __init__(self):
        self.A = [0]
        self.size = 0

    def heapify_down(self, i):
        """Max heapify down.

        Complexity: O(log(n)).
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

        if max_i != i:
            # Swap node i and node max_i.
            self.A[i], self.A[max_i] = self.A[max_i], self.A[i]
            self.heapify_down(max_i)

    def build(self, arr):
        """Build max heap from unordered array.

        Start from the level-1 nodes from leaves back to level-log(n) node.
        Specifically, node (n/2), node (n/2 - 1), ..., node 1, where
        n is the number of nodes including the root one.

        Complexity: O(n*log(n)) via simple analysis. Actually O(n).
        """
        self.A.extend(arr)
        self.size = len(arr)
        for i in reversed(range(1, (self.size + 1) // 2 + 1)):
            self.heapify_down(i)


def heapsort(arr):
    """Heapsort Algorithm.

    Notes:
      - Build max heap from unordered list.
      - Swap node 1 (max) and node n (last).
      - Discard node n from heap by decrementing heap_size.
      - Run heapify_down() to fix max heap violation in node 1.
      - Go to Step 2 unless heap is empty.
      - Output heapsorted A by ignoring redundant root.

    Complexity: O(n*log(n)),
      - since after n iterations the heap is empty,
      - and every iteration involves a swap and a heapify_down(),
        this takes O(log(n)) time.
    """
    max_pq = MaxHeap()
    max_pq.build(arr)

    while max_pq.size > 0:
        # Swap node 1 (max) and node n (last).
        max_pq.A[max_pq.size], max_pq.A[1] = (
            max_pq.A[1], max_pq.A[max_pq.size])

        # Discard node n from heap by decrementing heap_size
        max_pq.size -= 1
        
        max_pq.heapify_down(1)

    heapsort_arr = max_pq.A[1:]
    return heapsort_arr


def main():
    import random
    arr = [a for a in range(100)]
    random.shuffle(arr)
    print('Heapsort for unordered list:')
    print(heapsort(arr))


if __name__ == '__main__':
    main()
