from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class Stack(object):
    """Stack class."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        return self.items


def main():
    s = Stack()
    print('Is empty: {}'.format(s.is_empty()))
    
    s.push(4)
    s.push('dog')
    print('Peek: {}'.format(s.peek()))

    s.push(True)
    print('Size: {}'.format(s.size()))

    print('Is empty: {}'.format(s.is_empty()))

    s.push(8.4)

    print('Pop: {}'.format(s.pop()))
    print('Pop: {}'.format(s.pop()))

    print('Size: {}'.format(s.size()))
    print('Show: {}'.format(s.show()))


if __name__ == '__main__':
    main()
