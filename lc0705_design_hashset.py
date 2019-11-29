"""Leetcode 705. Design HashSet
Easy

URL: https://leetcode.com/problems/design-hashset/

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

- add(value): Insert a value into the HashSet. 
- contains(value) : Return whether the value exists in the HashSet or not.
- remove(value): Remove a value in the HashSet. 

If the value does not exist in the HashSet, do nothing.

Example:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:
- All values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashSet library.
"""

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Init hashset using list with load factor 2/3.
        self.capacity = 8
        self.size = 0
        self.set = [None] * self.capacity
        self.load_factor = 2.0 / 3

    def _hash(self, key):
        return key % self.capacity

    def _rehash(self, key):
        return (5 * key + 1) % self.capacity

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        # If hashset is larger than load factor, double it and copy old to new.
        if float(self.size) / self.capacity >= self.load_factor:
            self.capacity <<= 1
            new_set = [None] * self.capacity

            for h in range(self.capacity >> 1):
                if new_set[h]:
                    old_key = self.set[h]
                    new_h = self._hash(old_key)
                    while new_set[new_h]:
                        new_h = self._rehash(new_h)
                    new_set[new_h] = old_key

            self.set = new_set

        # Add key by Open Addressing with rehashing.
        hash_key = self._hash(key)

        while self.set[hash_key]:
            if self.set[hash_key] == key:
                return None
            else:
                hash_key = self._rehash(hash_key)

        self.set[hash_key] = key
        self.size += 1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_key = self._hash(key)

        while self.set[hash_key]:
            if self.set[hash_key] == key:
                self.set[hash_key] = None
                self.size -= 1
                return None
            else:
                hash_key = self._rehash(hash_key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash_key = self._hash(key)

        while self.set[hash_key]:
            if self.set[hash_key] == key:
                return True
            else:
                hash_key = self._rehash(hash_key)

        return False


def main():
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print hashSet.contains(1)     # returns true
    print hashSet.contains(3)     # returns false (not found)
    hashSet.add(2)
    print hashSet.contains(2)     # returns true
    hashSet.remove(2)
    print hashSet.contains(2)     # returns false (already removed)


if __name__ == '__main__':
    main()
