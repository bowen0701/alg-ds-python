from __future__ import print_function


class HashTable(object):
    """Create a HashTable class to implement Map data structure 
    with key-value mappings.
    """
    def __init__(self, table_size, weighted_bool=False):
        self.table_size = table_size
        self.slots = [None] * self.table_size
        self.data = [None] * self.table_size

    def hash(self, key, weighted_bool=False):
        """Hash function for integer or string."""
        if isinstance(key, int):
            """Hash an integer by mode division."""
            return key % self.table_size
        elif isinstance(key, str):
            """Hash a string by the Folding Method using 
            (weitghted) ordinal values plus mode division.
            """
            ord_sum = 0
            for pos in range(len(key)):
                if weighted_bool:
                    wt = pos + 1
                else:
                    wt = 1
                ord_sum += wt * ord(key[pos])
            return ord_sum % self.table_size

    def rehash(self, old_hash):
        """Rehash function using the linear probing method."""
        return (old_hash + 1) % self.table_size

    def put(self, key, data):
        hash_value = self.hash(key)

        if not self.slots[hash_value]:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # Replace data.
            else:
                next_slot = self.rehash(hash_value)
                while (self.slots[next_slot] and 
                       self.slots[next_slot] is not key):
                    next_slot = self.rehash(next_slot)

                if not self.slots[next_slot]:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # Replace data.

    def get(self, key):
        start_slot = self.hash(key)

        data = None
        stop_bool = False
        found_bool = False
        position = start_slot
        while (self.slots[position] and 
               not found_bool and not stop_bool):
            if self.slots[position] == key:
                found_bool = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop_bool = True

        return data

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)


def main():
    print('Hash Table with integer keys:')
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

    print('Hash Table with string keys:')
    h = HashTable(11)
    h['cat'] = 'c'
    h['dog'] = 'd'
    h['lion'] = 'l'
    h['tiger'] = 't'
    h['bird'] = 'b'   
    print('h.slots: {}'.format(h.slots))
    print('h.data: {}'.format(h.data))
    print('h["dog"]: {}'.format(h['dog']))
    print('h["cat"]: {}'.format(h['cat']))

    h['bird'] = 'bd'
    print('Replaced h["bird"]: {}'.format(h['bird']))
    print('h.data: {}'.format(h.data))

    print('h["pig"]: {}'.format(h['pig']))

    print('Hash Table with string keys by weighted folding method:')
    h = HashTable(11, weighted_bool=True)
    h['cat'] = 'c'
    h['dog'] = 'd'
    h['lion'] = 'l'
    h['tiger'] = 't'
    h['bird'] = 'b'   
    print('h.slots: {}'.format(h.slots))
    print('h.data: {}'.format(h.data))
    print('h["dog"]: {}'.format(h['dog']))
    print('h["cat"]: {}'.format(h['cat']))

    h['bird'] = 'bd'
    print('Replaced h["bird"]: {}'.format(h['bird']))
    print('h.data: {}'.format(h.data))

    print('h["pig"]: {}'.format(h['pig']))


if __name__ == '__main__':
    main()
