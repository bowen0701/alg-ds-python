from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


class Node(object):
    """Node class as building block for linked list."""
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class OrderedList(object):
    """Ordered list class.

    Implement ordered list by a linked list.
    Operations include the following:
      - is_empty()
      - size()
      - add(item)
      - append(item)
      - insert(item, pos)
      - pop(pos)
      - remove(ite)
      - search(item)
      - index(item)
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
            current = current.get_next()
        
        return counter

    def add(self, item):
        """Add item to list."""
        # temp = Node(item)
        # temp.set_next(self.head)
        # self.head = temp
        current = self.head
        previous = None
        stop_bool = False
        
        while current is not None and not stop_bool:
            if current.get_data() > item:
                stop_bool = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def remove(self, item):
        """Remove item from list, if existed."""
        current = self.head
        previous = None
        found_bool = False

        while not found_bool and current is not None:
            if current.get_data() == item:
                found_bool = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            print('{}: not existed'.format(item))
        elif previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def pop(self, pos=None):
        """Pop list item at specified position.

        If pos is None, then pop the last item.
        """
        current = self.head
        previous = None
        counter = 0

        if pos is None:
            pos = self.size() - 1

        while counter < pos and current is not None:
            previous = current
            current = current.get_next()
            counter += 1

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return current.get_data()

    def search(self, item):
        """Search item in list."""
        current = self.head
        found_bool = False
        stop_bool = False

        while not found_bool and not stop_bool and current is not None:
            if current.get_data() == item:
                found_bool = True
            else:
                if current.get_data() > item:
                    stop_bool = True
                else: 
                    current = current.get_next()
        
        return found_bool

    def index(self, item):
        """Obtain item's index in list."""
        current = self.head
        found_bool = False
        counter = 0

        while not found_bool and current is not None:
            if current.get_data() == item:
                found_bool = True
            else:
                counter += 1
                current = current.get_next()
        
        if not found_bool:
            counter = None
        return counter


def main():
    a_list = OrderedList()
    a_list.add(31)
    a_list.add(77)
    a_list.add(17)
    a_list.add(93)
    a_list.add(26)
    a_list.add(54)
    print('Is empty: {}'.format(a_list.is_empty()))
    print('Size: {}'.format(a_list.size()))

    print('Search existed 31: {}'.format(a_list.search(31)))
    print('Search non-existed 100: {}'.format(a_list.search(100)))

    print('Remove non-existed 100.')
    a_list.remove(100)
    print('Length: {}'.format(a_list.size()))
    
    print('Remove existed 31.')
    a_list.remove(31)
    print('Length: {}'.format(a_list.size()))
    print('Search removed 31: {}'.format(a_list.search(31)))

    print('Index of 100: {}'.format(a_list.index(100)))
    print('Index of 54: {}'.format(a_list.index(54)))

    print('Add 31 back.')
    a_list.add(31)
    print('Index of 31: {}'.format(a_list.index(31)))

    print('Pop item at pos 0.')
    print(a_list.pop(0))
    print('Length: {}'.format(a_list.size())) 
    
    print('Pop item at last pos.')
    print(a_list.pop())
    print('Length: {}'.format(a_list.size()))
    print(a_list.pop())
    print('Length: {}'.format(a_list.size()))
    print(a_list.pop())
    print('Length: {}'.format(a_list.size()))
    print(a_list.pop())
    print('Length: {}'.format(a_list.size()))
    print(a_list.pop())
    print('Length: {}'.format(a_list.size()))


if __name__ == '__main__':
    main()
