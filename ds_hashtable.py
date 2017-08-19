from __future__ import print_function


class HashTable(object):
    """Create a HashTable class to implement Map data structure 
    with key-value mappings.
    """
    def __init__(self, table_size):
        self.size = table_size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hash(self, key, size):
        return key % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, data):
        hash_value = self.hash(key, len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # Replace data.
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while ((self.slots[next_slot] is not None) and 
                       (self.slots[next_slot] is not key)):
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # Replace data.

    def get(self, key):
        start_slot = self.hash(key, len(self.slots))

        data = None
        stop-bool = False
        found-bool = False
        position = start_slot
        while (self.slots[position] is not None and 
               not found-bool and not stop-bool):
            if self.slots[position] == key:
                found-bool = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop-bool = True

        return data

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)


def main():
    h = HashTable(11)
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'
    
    print('h.slots: {}'.format(h.slots))
    print('h.data: {}'.format(h.data))
    print('h[20]: {}'.format(h[20]))
    print('h[17]: {}'.format(h[17]))

    h[20] = 'duck'
    print('Replaced h[20]: {}'.format(h[20]))
    print('h.data: {}'.format(h.data))

    print('h[99]: {}'.format(h[99]))


if __name__ == '__main__':
    main()
