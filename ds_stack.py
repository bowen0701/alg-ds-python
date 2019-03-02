from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class StackLs(object):
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
    s = StackLs()
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
