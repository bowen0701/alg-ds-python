from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

class BinaryHeap(object):
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
            min_child = _get_min_child(i)
            if self.heap_ls[i] > self.heap_ls[min_child]:
                tmp = self.heap_ls[1]
                self.heap_ls[1] = self.heap_ls[min_child]
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

    def build_entire_heap():
        pass


def main():
    pass


if __name__ == '__main__':
    main()

