from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from collections import deque


class Queue(object):
    """Queue using list."""
    def __init__(self):
        self.queue = deque([])

    def is_empty(self):
        return self.queue == deque([])

    def peek(self):
        return self.queue[-1]

    def enqueue(self, item):
        self.queue.appendleft(item)

    def dequeue(self):
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)

    def show(self):
        return list(self.queue)


class ListNode(object):
    """List Node for Queue_LL class."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue_LL(object):
    """Queue using linked list.

    Queue: Head->Node1->Node2->Tail
      - Enqueue: from Tail
      - Dequeue: from Head
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        if not self.head:
            return None
        return self.head.data

    def enqueue(self, data):
        node = ListNode(data)

        if not self.tail:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        if not self.head:
            self.head = node

    def dequeue(self):
        if not self.head:
            return None

        data = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None

        return data

    def size(self):
        counter = 0
        head = self.head
        while head:
            counter += 1
            head = head.next
        return counter

    def show(self):
        queue = []
        head = self.head
        while head:
            queue.insert(0, head.data)
            head = head.next
        return queue


def main():
    # Initiate Queue instance by Queue() or Queue_LL().
    q = Queue()
    print('Is empty: {}'.format(q.is_empty()))
    q.enqueue('dog')
    q.enqueue(4)
    q.enqueue(8.4)
    print('Is empty: {}'.format(q.is_empty()))
    print('Show: {}'.format(q.show()))
    print('Size: {}'.format(q.size()))
    print('Peek: {}'.format(q.peek()))
    print('Dequeue: {}'.format(q.dequeue()))
    print('Dequeue: {}'.format(q.dequeue()))
    print('Is empty: {}'.format(q.is_empty()))
    print('Show: {}'.format(q.show()))
    print('Size: {}'.format(q.size()))

    q = Queue_LL()
    print('Is empty: {}'.format(q.is_empty()))
    q.enqueue('dog')
    q.enqueue(4)
    q.enqueue(8.4)
    print('Is empty: {}'.format(q.is_empty()))
    print('Show: {}'.format(q.show()))
    print('Size: {}'.format(q.size()))
    print('Peek: {}'.format(q.peek()))
    print('Dequeue: {}'.format(q.dequeue()))
    print('Dequeue: {}'.format(q.dequeue()))
    print('Is empty: {}'.format(q.is_empty()))
    print('Show: {}'.format(q.show()))
    print('Size: {}'.format(q.size()))


if __name__ == '__main__':
    main()
