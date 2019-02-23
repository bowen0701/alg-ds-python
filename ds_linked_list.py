from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from numpy import inf


class Node(object):
    """Node class as building block for linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    """Singly linked list class.

    Operations include the following:
      - is_empty()
      - size()
      - prepend(data)
      - append(data)
      - delete_with_data(data)
      - insert(pos, data)
      - pop(pos)
      - search(node)
      - index(node)
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check list is empty or not."""
        return self.head is None

    def size(self):
        """Obtain list size."""
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next    
        return counter

    def prepend(self, data):
        """Prepend data to list head.

        Time complexity: O(1).
        """
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def append(self, data):
        """Append data to list tail.

        Time complexity: O(n).
        """
        if self.head is None:
            self.head = Node(data)
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def delete_with_data(self, data):
        """Remove data from list, if existed.

        Time complexity: O(n).
        """
        if self.head is None:
            return None
        if self.head.data == data:
            # Skip deleted node.
            self.head = self.head.next
            return None

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                # Skip deleted node.
                current.next = current.next.next
                return None
            else:
                current = current.next

    def insert(self, pos, data):
        """Insert data to specified position of list.

        Time complexity = O(pos).
        """
        current = self.head
        previous = None
        counter = 0

        while counter < pos and current.next is not None:
            previous = current
            current = current.next
            counter += 1

        insert_node = Node(data)
        insert_node.next = current
        if pos == 0:
            self.head = insert_node
        else:
            previous.next = insert_node

    def pop(self, pos=None):
        """Pop list node at specified position.

        Time complexity: O(pos).
        """
        if pos is None:
            pos = self.size() - 1

        current = self.head
        previous = None
        counter = 0

        while counter < pos and current.next is not None:
            previous = current
            current = current.next
            counter += 1

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next       
        return current.data

    # TODO: Refactor the following search, index.

    def search(self, data):
        """Search data in list."""
        current = self.head
        found_bool = False

        while not found_bool and current.next is not None:
            if current.data == data:
                found_bool = True
            else:
                current = current.next
        
        return found_bool

    def index(self, node):
        """Obtain node's index in list."""
        current = self.head
        found_bool = False
        counter = 0

        while not found_bool and current is not None:
            if current.get_data() == node:
                found_bool = True
            else:
                counter += 1
                current = current.get_next()
        
        if not found_bool:
            counter = None
        return counter


def main():
    # - is_empty()
    # - size()
    # - prepend(data)
    # - append(data)
    # - delete_with_data(data)
    # - insert(pos, data)
    # - pop(pos)

    a_list = LinkedList()
    a_list.prepend(31)
    a_list.prepend(77)
    a_list.prepend(17)
    a_list.prepend(93)
    a_list.prepend(26)
    a_list.prepend(54)
    print('Is empty: {}'.format(a_list.is_empty()))
    print('Size: {}'.format(a_list.size()))
    
    pass


if __name__ == '__main__':
    main()
