from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

class PriorityQueue(object):
	"""Binary Min Heap class."""
    def __init__(self, ):
        self.heap_ls = [(0, 0)]
        self.current_size = 0

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_ls[i][0] < self.heap_ls[i // 2][0]:
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
            if self.heap_ls[i * 2][0] < self.heap_ls[i * 2 + 1][0]:
                return i * 2
            else:
                return i * 2 + 1

    def _percolate_down(self, i):
        while (i * 2) <= self.current_size:
            min_child = self._get_min_child(i)
            if self.heap_ls[i][0] > self.heap_ls[min_child][0]:
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

    def build_heap(self, a_list):
        # alist: a list of tuples.
        self.current_size = len(a_list)
        self.heap_ls = [(0, 0)] + a_list[:]
        i = len(a_list) // 2
        while i > 0:
            self._percolate_down(i)
            i -= 1

    def decrease_key(self, val, key):
        pass


def main():
    pass

if __name__ == '__main__':
	main()
