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


def main():
    pass


if __name__ == '__main__':
    main()

