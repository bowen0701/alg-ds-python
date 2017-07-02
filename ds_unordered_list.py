from __future__ import print_function


class Node(object):
    """Node class as building block for unordered list."""
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList(object):
    """Unordered list class.

    Implement unordered list by a linked list.
    Operations include the following:
      - add(item)
      - remove(ite)
      - search(item)
      - is_empty()
      - length()
      - append(item)
      - index(item)
      - insert(item, pos)
      - pop(pos)
    """
    def __init__(self):
        pass

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass

    def is_empty(self):
        pass

    def length(self):
        pass

    def append(self, item):
        pass

    def index(self, item):
        pass

    def insert(self, pos, item):
        pass

    def pop(self, pos):
        pass
