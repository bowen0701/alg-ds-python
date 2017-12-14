from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class Deque(object):
    """Deque class.

    It consists of 6 operations:
      - add_front()
      - add_rear()
      - remove_front()
      - remove_rear()
      - is_empty()
      - size()
    """
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def main():
    d = Deque()
    print(d.is_empty())

    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d.is_empty())
    print(d.size())

    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())

if __name__ == '__main__':
    main()

