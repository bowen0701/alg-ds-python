from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class Queue(object):
    """Queue class."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)


def main():
    queue = Queue()

    queue.is_empty()

    queue.enqueue('dog')
    queue.enqueue(4)
    queue.enqueue(8.4)

    print('Queue size: {}'.format(queue.size()))

    print('Dequeue: {}'.format(queue.dequeue()))
    print('Queue size: {}'.format(queue.size()))

if __name__ == '__main__':
    main()
