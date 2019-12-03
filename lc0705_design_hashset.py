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
hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // return true
hashSet.contains(3);    // return false (not found)
hashSet.add(2);          
hashSet.contains(2);    // return true
hashSet.remove(2);          
hashSet.contains(2);    // returne false (already removed)

Note:
- All values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashSet library.
"""

class MyHashSet(object):

    def __init__(self):
        """
        Initialize data structure.
        """
        self.capacity = 8
        self.size = 0
        self.set = [None] * 8
        self.load_factor = 2.0 / 3
        
    def _hash(self, key):
        """
        Hash function: key->hashed key.
        """
        return key % self.capacity

    def _rehash(self, hash_key):
        """
        Rehash function when there is collision: hashed key->rehashed key.
        """
        return (5 * hash_key + 1) % self.capacity

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        # If hashset size is larger than capacity, double it and copy keys.
        if float(self.size) / self.capacity >= self.load_factor:
            self.capacity <<= 1
            new_set = [None] * self.capacity
            
            for i in range(self.capacity >> 1):
                if self.set[i] >= 0:
                    h = self._hash(self.set[i])

                    while new_set[h] is not None:
                        h = self._rehash(h)
                    
                    new_set[h] = self.set[i]

            self.set = new_set

        # Get hashed key and apply Open Addressing for collision.
        h = self._hash(key)

        while self.set[h] is not None:
            if self.set[h] == key:
                return None
            else:
                h = self._rehash(h)
                if self.set[h] == -1:
                    break

        self.set[h] = key
        self.size += 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        h = self._hash(key)

        while self.set[h]:
            if self.set[h] == key:
                self.set[h] = -1
                self.size -= 1
                return None
            else:
                h = self._rehash(h)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        h = self._hash(key)

        while self.set[h] is not None:
            if self.set[h] == key:
                return True
            else:
                h = self._rehash(h)

        return False


def main():
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    print hashSet.contains(1)     # returnew_set true
    print hashSet.contains(3)     # returnew_set false (not found)
    hashSet.add(2)
    print hashSet.contains(2)     # returnew_set true
    hashSet.remove(2)
    print hashSet.contains(2)     # returnew_set false (already removed)


if __name__ == '__main__':
    main()
