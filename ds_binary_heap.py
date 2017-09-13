from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class BinaryMinHeap(object):
    def __init__(self):
        # Put single zero as the 1st element, so that 
        # integer division can be used in later methods.
        self.heap_ls = [0]
        self.current_size = 0

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

    def delete_min(self):
        val_del = self.heap_ls[1]
        self.heap_ls[1] = self.heap_ls[self.current_size]
        self.current_size -= 1
        self.heap_ls.pop()
        self._percolate_down(1)
        return val_del

    def build_entire_heap(self, a_list):
        self.current_size = len(a_list)
        self.heap_ls = [0] + a_list[:]
        i = len(a_list) // 2
        while i > 0:
            self._percolate_down(i)
            i -= 1


def main():
    bh = BinaryMinHeap()
    bh.insert(5)
    print('Heap: {}'.format(bh.heap_ls))    
    bh.insert(9)
    print('Heap: {}'.format(bh.heap_ls))
    bh.insert(11)
    print('Heap: {}'.format(bh.heap_ls))
    bh.insert(14)
    print('Heap: {}'.format(bh.heap_ls))
    bh.insert(18)
    print('Heap: {}'.format(bh.heap_ls))
    bh.insert(19)
    print('Heap: {}'.format(bh.heap_ls))
    bh.insert(21)
    print('Heap: {}'.format(bh.heap_ls))
    bh.insert(33)
    print('Heap: {}'.format(bh.heap_ls))
    bh.insert(17)
    print('Heap: {}'.format(bh.heap_ls))
    bh.insert(27)
    print('Heap: {}'.format(bh.heap_ls))

    print(bh.delete_min())
    print('Heap: {}'.format(bh.heap_ls))


if __name__ == '__main__':
    main()

