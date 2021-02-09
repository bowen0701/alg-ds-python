from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class Stack(object):
    """Stack using list."""
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def peek(self):
        return self.stack[-1]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack


class ListNode(object):
    """List Node for StackLL class."""
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLL(object):
    """Stack using linked list.

    Stack: Top->Node2->Node1->None.
    """
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def peek(self):
        if not self.top:
            return None
        return self.top.data

    def push(self, data):
        node = ListNode(data)
        if not self.top:
            top = node
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def size(self):
        counter = 0
        top = self.top
        while top:
            counter += 1
            top = top.next
        return counter

    def show(self):
        if not self.top:
            return []
        stack = []
        top = self.top
        while top:
            stack.insert(0, top.data)
            top = top.next
        return stack


def main():
    s = Stack()
    print('Is empty: {}'.format(s.is_empty()))
    s.push('dog')
    s.push(4)
    s.push(8.4)
    print('Show: {}'.format(s.show()))
    print('Peek: {}'.format(s.peek()))
    print('Is empty: {}'.format(s.is_empty()))
    print('Size: {}'.format(s.size()))
    print('Pop: {}'.format(s.pop()))
    print('Pop: {}'.format(s.pop()))
    print('Is empty: {}'.format(s.is_empty()))
    print('Size: {}'.format(s.size()))
    print('Show: {}'.format(s.show()))

    s = StackLL()
    print('Is empty: {}'.format(s.is_empty()))
    s.push('dog')
    s.push(4)
    s.push(8.4)
    print('Show: {}'.format(s.show()))
    print('Peek: {}'.format(s.peek()))
    print('Is empty: {}'.format(s.is_empty()))
    print('Size: {}'.format(s.size()))
    print('Pop: {}'.format(s.pop()))
    print('Pop: {}'.format(s.pop()))
    print('Is empty: {}'.format(s.is_empty()))
    print('Size: {}'.format(s.size()))
    print('Show: {}'.format(s.show()))


if __name__ == '__main__':
    main()
