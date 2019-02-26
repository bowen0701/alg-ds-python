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
      - delete_with_data(data)
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
        a_list = []
        current = self.head
        while current:
            a_list.append(current.data)
            current = current.next
        print(a_list)


    def prepend(self, data):
        """Prepend data to list head.

        Time complexity: O(1).
        Space complexity: O(1).
        """
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def append(self, data):
        """Append data to list tail.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if self.head is None:
            self.head = Node(data)
            return None
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def delete_with_data(self, data):
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
        found_bool = False

        while not found_bool and current.next:
            if current.data == data:
                found_bool = True
            else:
                current = current.next

        return found_bool

    def index(self, data):
        """Obtain node's index in list.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if self.head is None:
            return None

        current = self.head
        found_bool = False
        counter = 0

        while not found_bool and current.next:
            if current.data == data:
                found_bool = True
            else:
                current = current.next
                counter += 1
        
        if not found_bool:
            counter = None

        return counter


def main():
    a_list = LinkedList()
    a_list.prepend(31)
    a_list.prepend(77)
    a_list.prepend(17)
    a_list.prepend(93)
    a_list.prepend(26)
    a_list.prepend(54)
    a_list.show()
    print('Is empty: {}'.format(a_list.is_empty()))
    print('Size: {}'.format(a_list.size()))
    
    print('Append 45:')
    a_list.append(45)
    print('Size: {}'.format(a_list.size()))
    a_list.show()

    print('Delete non-existed 100:')
    a_list.delete_with_data(100)
    a_list.show()

    print('Delete 31:')
    a_list.delete_with_data(31)
    a_list.show()

    print('Delete 45:')
    a_list.delete_with_data(45)
    a_list.show()

    print('Insert 27 at pos 3:')
    a_list.insert(3, 27)
    a_list.show()

    print('Pop pos 3:')
    a_list.pop(3)
    a_list.show()

    print('Search non-existed 100: {}'.format(a_list.search(100)))
    print('Search 93: {}'.format(a_list.search(93)))

    print('Index non-existed 100: {}'.format(a_list.index(100)))
    print('Index 93: {}'.format(a_list.index(93)))


if __name__ == '__main__':
    main()
