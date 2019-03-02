from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class QueueLs(object):
    """Queue class."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def show(self):
        return self.items


def main():
    q = QueueLs()
    print('Is empty: {}'.format(q.is_empty()))

    q.enqueue('dog')
    q.enqueue(4)
    q.enqueue(8.4)

    print('Show: {}'.format(q.show()))
    print('Peek: {}'.format(q.peek()))
    print('Is empty: {}'.format(q.is_empty()))
    print('Size: {}'.format(q.size()))

    print('Dequeue: {}'.format(q.dequeue()))
    print('Dequeue: {}'.format(q.dequeue()))

    print('Is empty: {}'.format(q.is_empty()))
    print('Size: {}'.format(q.size()))
    print('Show: {}'.format(q.show()))


if __name__ == '__main__':
    main()
