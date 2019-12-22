from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class HashTable(object):
    """HashTable with Open Addressing method for collision."""
    def __init__(self, size, is_weighted=False):
        self.size = size
        self.slots = [None] * self.size
        self.maps = [None] * self.size

    def _hash(self, key, is_weighted=False):
        """Hash function for integer or string."""
        if isinstance(key, int):
            # Hash an integer by mode division.
            return key % self.size
        elif isinstance(key, str):
            # Hash a string by the Folding Method using 
            # (weitghted) ordinal values plus mode division.
            ord_sum = 0
            for pos in range(len(key)):
                if is_weighted:
                    wt = pos + 1
                else:
                    wt = 1
                ord_sum += wt * ord(key[pos])
            return ord_sum % self.size

    def _rehash(self, hash_code):
        """Rehash function using the linear probing method."""
        return (3 * hash_code + 1) % self.size

    def put(self, key, value):
        """
        Time complexity: average case O(1), worst case O(size).
        Space complexity: O(1).
        """
        h = self._hash(key)

        # If key_hash's slot is empty, set slots & map as key & value.
        if not self.slots[h]:
            self.slots[h] = key
            self.maps[h] = value
        else:
            # If key_hash's slot is key, update its value.
            if self.slots[h] == key:
                self.maps[h] = value
            else:
                # If collision exists for hashed code, keep rehashing till
                # new hashed code's slot is empty or is key.
                next_h = self._rehash(h)
                while (self.slots[next_h] and self.slots[next_h] != key):
                    next_h = self._rehash(next_h)

                if not self.slots[next_h]:
                    self.slots[next_h] = key
                    self.maps[next_h] = value
                else:
                    self.maps[next_h] = value

    def get(self, key):
        """
        Time complexity: average case O(1), worst case O(size).
        Space complexity: O(1).
        """
        h = self._hash(key)

        while self.slots[h]:
            if self.slots[h] == key:
                return self.maps[h]
            else:
                h = self._rehash(h)

        return None

    def delete(self, key):
        """
        Time complexity: average case O(1), worst case O(size).
        Space complexity: O(1).
        """
        h = self._hash(key)

        while self.slots[h]:
            if self.slots[h] == key:
                self.slots[h] = None
                self.maps[h] = None
                return None
            else:
                h = self._rehash(h)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)


def main():
    print('HashTable with integer keys:')
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
    print('- h.slots: {}'.format(h.slots))
    print('- h.maps: {}'.format(h.maps))
    print('- h[20]: {}'.format(h[20]))
    print('- h[17]: {}'.format(h[17]))

    h[20] = 'duck'
    print('- replace h[20]: {}'.format(h[20]))
    print('- h.maps: {}'.format(h.maps))

    print('- h[99]: {}'.format(h[99]))

    print('HashTable with string keys:')
    h = HashTable(11)
    h['cat'] = 'c'
    h['dog'] = 'd'
    h['lion'] = 'l'
    h['tiger'] = 't'
    h['bird'] = 'b'   
    print('- h.slots: {}'.format(h.slots))
    print('- h.maps: {}'.format(h.maps))
    print('- h["dog"]: {}'.format(h['dog']))
    print('- h["cat"]: {}'.format(h['cat']))

    h['bird'] = 'bd'
    print('- replacee h["bird"]: {}'.format(h['bird']))
    print('- h.maps: {}'.format(h.maps))

    print('- h["pig"]: {}'.format(h['pig']))

    print('HashTable with string keys by weighted folding method:')
    h = HashTable(11, is_weighted=True)
    h['cat'] = 'c'
    h['dog'] = 'd'
    h['lion'] = 'l'
    h['tiger'] = 't'
    h['bird'] = 'b'   
    print('- h.slots: {}'.format(h.slots))
    print('- h.maps: {}'.format(h.maps))
    print('- h["dog"]: {}'.format(h['dog']))
    print('- h["cat"]: {}'.format(h['cat']))

    h['bird'] = 'bd'
    print('- replace h["bird"]: {}'.format(h['bird']))
    print('- h.maps: {}'.format(h.maps))

    print('- h["pig"]: {}'.format(h['pig']))

    del h['bird']
    print('- h.slots: {}'.format(h.slots))
    print('- h.maps: {}'.format(h.maps))


if __name__ == '__main__':
    main()
