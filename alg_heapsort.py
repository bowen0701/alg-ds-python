from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ds_max_heap import MaxHeap 


def heapsort(A):
    """Heapsort Algorithm.

    Notes:
      - Build max heap from unordered list.
      - Swap node 1 (max) and node n (last).
      - Discard node n from heap by decrementing heap_size.
      - Run heapify() to restore max heap property in node 1.
      - Go to Step 2 unless heap is 1 element only.
      - Output heapsorted A by ignoring redundant root.

    Complexity: O(n*log(n)),
      - build(): takes O(n)
      - each of the (n - 1) calls to heapify() takes O(log(n))
    """
    max_heap = MaxHeap()
    max_heap.build(A)

    while max_heap.size > 1:
        # Swap node 1 (max) and node n (last).
        max_heap.A[max_heap.size], max_heap.A[1] = max_heap.A[1], max_heap.A[max_heap.size]

        # Discard node n from heap by decrementing heap_size
        max_heap.size -= 1
        
        # Heapify starting from node 1.
        max_heap.heapify(1)

    sorted_A = max_heap.A[1:]
    return sorted_A


def main():
    import random
    A = [a for a in range(100)]
    random.shuffle(A)
    print('Heapsort for unordered list:')
    print(heapsort(A))


if __name__ == '__main__':
    main()
