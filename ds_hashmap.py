from __future__ import print_function


class HashMap(object):
    """Create a HashMap class to implement Map data structure 
    with key-value mappings.
    """
    def __init__(self, size, weighted_bool=False):
        self.size = size
        self.slots = [None] * self.size
        self.maps = [None] * self.size

    def hash(self, key, weighted_bool=False):
        """Hash function for integer or string."""
        if isinstance(key, int):
            """Hash an integer by mode division."""
            return key % self.size
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
            return ord_sum % self.size

    def rehash(self, old_hash):
        """Rehash function using the linear probing method."""
        return (old_hash + 1) % self.size

    def put(self, key, value):
        # Time complexity: averate case O(1), worst case O(size).
        # Space complexity: O(1).
        key_hash = self.hash(key)

        # If key_hash's slot does not exist, set slots & map as key & value.
        if not self.slots[key_hash]:
            self.slots[key_hash] = key
            self.maps[key_hash] = value
        else:
            # If key_hash's slot is key, update its value.
            if self.slots[key_hash] == key:
                self.maps[key_hash] = value
            else:
                # If collision exists for key_hash, keep rehashing till
                # new key_hash's slot does not exist or is key.
                next_slot = self.rehash(key_hash)
                while (self.slots[next_slot] and 
                       self.slots[next_slot] is not key):
                    next_slot = self.rehash(next_slot)

                if not self.slots[next_slot]:
                    self.slots[next_slot] = key
                    self.maps[next_slot] = value
                else:
                    self.maps[next_slot] = value

    def get(self, key):
        # Time complexity: averate case O(1), worst case O(size).
        # Space complexity: O(1).
        start_key_hash = self.hash(key)

        value = None
        stop_bool = False
        found_bool = False
        key_hash = start_key_hash
        while (self.slots[key_hash] and 
               not found_bool and not stop_bool):
            if self.slots[key_hash] == key:
                found_bool = True
                value = self.maps[key_hash]
            else:
                key_hash = self.rehash(key_hash)
                if key_hash == start_key_hash:
                    stop_bool = True

        return value

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


def main():
    print('HashMap with integer keys:')
    h = HashMap(11)
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

    print('Hash Map with string keys:')
    h = HashMap(11)
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

    print('Hash Map with string keys by weighted folding method:')
    h = HashMap(11, weighted_bool=True)
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


if __name__ == '__main__':
    main()
