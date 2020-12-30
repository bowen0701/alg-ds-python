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
      - show()
      - prepend(data)
      - append(data)
      - delete_node(data)
      - insert(pos, data)
      - pop(pos)
      - search(data)
      - index(data)
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check list is empty or not.

        Time complexity: O(1).
        Space complexity: O(1).
        """
        return self.head is None

    def size(self):
        """Obtain list size.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next    
        return counter

    def show(self):
        """Show the list.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        ll = []
        current = self.head
        while current:
            ll.append(current.data)
            current = current.next
        print(ll)


    def prepend(self, data):
        """Prepend data to list head.

        Time complexity: O(1).
        Space complexity: O(1).
        """
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        return None

    def append(self, data):
        """Append data to list tail.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # If linked list is empty.
        if not self.head:
            self.head = Node(data)
            return None

        # If linked list exits, append new node after the tail node.
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)
        return None

    def delete_node(self, data):
        """Remove data from list, if existed.

        If pos is None, then pop the last item.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not self.head:
            return None

        if self.head.data == data:
            # Skip deleted node.
            self.head = self.head.next
            return None

        current = self.head
        while current.next:
            if current.next.data == data:
                # Skip deleted node.
                current.next = current.next.next
                return None
            else:
                current = current.next
        return None

    def insert(self, pos, data):
        """Insert data to specified position of list.

        Time complexity = O(pos).
        Space complexity: O(1).
        """
        if not self.head and pos > 0:
            print('Cannot insert to empty list.')
            return None

        current = self.head
        previous = None
        counter = 0

        if not self.head:
            self.prepend(data)

        while counter < pos and current.next:
            previous = current
            current = current.next
            counter += 1

        insert_node = Node(data)
        insert_node.next = current
        if pos == 0:
            self.head = insert_node
        else:
            previous.next = insert_node
        return None

    def pop(self, pos=None):
        """Pop list node at specified position.

        Time complexity: O(pos).
        Space complexity: O(1).
        """
        if not self.head:
            return None
        if not pos:
            pos = self.size() - 1

        current = self.head
        previous = None
        counter = 0

        while counter < pos and current.next:
            previous = current
            current = current.next
            counter += 1

        if not previous:
            self.head = current.next
        else:
            previous.next = current.next       
        return current.data

    def search(self, data):
        """Search data in list.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not self.head:
            return False

        current = self.head
        is_found = False

        while not is_found and current.next:
            if current.data == data:
                is_found = True
            else:
                current = current.next

        return is_found

    def index(self, data):
        """Obtain node's index in list.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if not self.head:
            return None

        current = self.head
        is_found = False
        counter = 0

        while not is_found and current.next:
            if current.data == data:
                is_found = True
            else:
                current = current.next
                counter += 1
        
        if not is_found:
            counter = None

        return counter


def main():
    ll = LinkedList()
    ll.append(31)
    ll.append(77)
    ll.append(17)
    ll.append(93)
    ll.append(26)
    ll.append(54)
    ll.show()

    ll = LinkedList()
    ll.prepend(31)
    ll.prepend(77)
    ll.prepend(17)
    ll.prepend(93)
    ll.prepend(26)
    ll.prepend(54)
    ll.show()
    print('Is empty: {}'.format(ll.is_empty()))
    print('Size: {}'.format(ll.size()))

    print('Append 45:')
    ll.append(45)
    print('Size: {}'.format(ll.size()))
    ll.show()

    print('Delete non-existed 100:')
    ll.delete_node(100)
    ll.show()

    print('Delete 31:')
    ll.delete_node(31)
    ll.show()

    print('Delete 45:')
    ll.delete_node(45)
    ll.show()

    print('Insert 27 at pos 3:')
    ll.insert(3, 27)
    ll.show()

    print('Pop pos 3:')
    ll.pop(3)
    ll.show()

    print('Search non-existed 100: {}'.format(ll.search(100)))
    print('Search 93: {}'.format(ll.search(93)))

    print('Index non-existed 100: {}'.format(ll.index(100)))
    print('Index 93: {}'.format(ll.index(93)))


if __name__ == '__main__':
    main()
