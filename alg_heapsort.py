from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def parent(i):
    return i // 2

def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1


def max_heapify(A, heap_size, i):
    """Max heapify operation.

    Complexity: O(log(n)).
    """
    l = left(i)
    r = right(i)
    if l <= heap_size and A[l] > A[i]:
        max_i = l
    else:
        max_i = i
    if r <= heap_size and A[r] > A[max_i]:
        max_i = r
    if max_i != i:
        # Swap node i and node max_i.
        A[i], A[max_i] = A[max_i], A[i]
        max_heapify(A, heap_size, max_i)


def build_max_heap(A):
    """Build max heap from unordered array.

    Start from the level-1 nodes from leaves back to level-log(n) node.
    Specifically, node (n/2), node (n/2 - 1), ..., node 1, where
    n is the number of nodes including the root one.

    Complexity: O(n*log(n)) via simple analysis. Actually O(n).
    """
    max_pq = [0]
    max_pq.extend(A)
    heap_size = len(A)
    for i in reversed(range(1, (heap_size + 1) // 2 + 1)):
        max_heapify(max_pq, heap_size, i)
    return max_pq, heap_size


def heapsort(A):
    """Heapsort Algorithm.

    Notes:
      - Build max heap from unordered list.
      - Swap node n and node 1.
      - Discard node n from heap by decrementing heap_size.
      - Run max_heapify to fix max heap violation in node 1.
      - Go to Step 2 unless heap is empty.
      - Output heapsorted A by ignoring redundant root.

    Complexity: O(n*log(n)),
      - since after n iterations the heap is empty,
      - and every iteration involves a swap and a max_heapify operation,
        hence it takes O(log(n)) time.
    """
    max_pq, heap_size = build_max_heap(A)

    while heap_size > 0:
        max_pq[heap_size], max_pq[1] = max_pq[1], max_pq[heap_size]
        heap_size -= 1
        max_heapify(max_pq, heap_size, 1)

    heapsort_A = max_pq[1:]
    return heapsort_A


def main():
    print('Heapsort for unordered list [5, 7, 3, 1]:')
    print(heapsort([5, 7, 3, 1]))


if __name__ == '__main__':
    main()
