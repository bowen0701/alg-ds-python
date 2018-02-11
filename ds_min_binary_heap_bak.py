from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class MinBinaryHeap(object):
    """Binary Min Heap class."""
    def __init__(self):
        # Put single zero as the 1st element, so that 
        # integer division can be used in later methods.
        self.heap_ls = [0]
        self.current_size = 0

    def heap_show(self):
        print(self.heap_ls)

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_ls[i] < self.heap_ls[i // 2]:
                tmp = self.heap_ls[i // 2]
                self.heap_ls[i // 2] = self.heap_ls[i]
                self.heap_ls[i] = tmp
            i = i // 2

    def insert(self, new_node):
        self.heap_ls.append(new_node)
        self.current_size += 1
        self._percolate_up(self.current_size)

    def _get_min_child(self, i):
        if (i * 2 + 1) > self.current_size:
            return i * 2
        else:
            if self.heap_ls[i * 2] < self.heap_ls[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def _percolate_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self._get_min_child(i)
            if self.heap_ls[i] > self.heap_ls[min_child]:
                tmp = self.heap_ls[i]
                self.heap_ls[i] = self.heap_ls[min_child]
                self.heap_ls[min_child] = tmp
            else:
                pass
            i = min_child

    def find_min(self):
        return self.heap_ls[1]
    
    def delete_min(self):
        val_del = self.heap_ls[1]
        self.heap_ls[1] = self.heap_ls[self.current_size]
        self.current_size -= 1
        self.heap_ls.pop()
        self._percolate_down(1)
        return val_del

    def is_empty(self):
        return self.current_size == 0

    def size(self):
        return self.current_size

    def __contains__(self, node):
        return node in self.heap_ls

    def build_heap(self, a_list):
        self.current_size = len(a_list)
        self.heap_ls = [0] + a_list[:]
        i = len(a_list) // 2
        while i > 0:
            self._percolate_down(i)
            i -= 1


def main():
    bh_min = MinBinaryHeap()
    bh_min.insert(5)
    bh_min.insert(9)
    bh_min.insert(11)
    bh_min.insert(14)
    bh_min.insert(18)
    bh_min.insert(19)
    bh_min.insert(21)
    bh_min.insert(33)
    bh_min.insert(17)
    bh_min.insert(27)

    print('Binary heap:')
    bh_min.heap_show()

    print('Find min: {}'.format(bh_min.find_min()))
    print('Is empty? {}'.format(bh_min.is_empty()))
    print('Size? {}'.format(bh_min.size()))

    bh_min.insert(7)
    print('Insert 7: {}'.format(bh_min.heap_ls))

    print('Min: {}'.format(bh_min.delete_min()))
    print('Delete min: {}'.format(bh_min.heap_ls))

    bh_min = MinBinaryHeap()
    bh_min.build_heap([9, 6, 5, 2, 3])
    print('Build heap: {}'.format(bh_min.heap_ls))

    print('9 in bh_min: {}'.format(9 in bh_min))
    print('1 in bh_min: {}'.format(1 in bh_min))


if __name__ == '__main__':
    main()

