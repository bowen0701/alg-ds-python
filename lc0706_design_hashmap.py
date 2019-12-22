"""Leetcode 706. Design HashMap
Easy

URL: https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

- put(key, value) : Insert a (key, value) pair into the HashMap. 
  If the value already exists in the HashMap, update the value.
- get(key): Returns the value to which the specified key is mapped, 
  or -1 if this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key 
  if this map contains the mapping for the key.

Example:
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);         // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);         // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:
- All keys and values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashMap library.
"""

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 8
        self.size = 0
        self.map = [[None, None]] * 8
        self.load_factor = 2.0 / 3

    def _hash(self, key):
        return key % self.capacity

    def _rehash(self, hash_code):
        return (5 * hash_code + 1) % self.capacity

    def put(self, key, value):
        """
        Value will always be non-negative.

        :type key: int
        :type value: int
        :rtype: None
        """
        # If hashmap size is larger than capacity, double it and copy keys & values.
        if float(self.size) / self.capacity >= self.load_factor:
            self.capacity <<= 1
            new_map = [[None, None]] * self.capacity

            for i in range(self.capacity >> 1):
                if self.map[i][0] >= 0:
                    h = self._hash(self.map[i][0])

                    while new_map[h][0] is not None:
                        h = self._rehash(h)

                    new_map[h] = self.map[i]

            self.map = new_map

        # Get hashed key and apply Open Addressing for collision.
        h = self._hash(key)

        while self.map[h][0] is not None:
            if self.map[h][0] == key:
                self.map[h][1] = value
                return None
            else:
                h = self._rehash(h)
                if self.map[h][0] == -1:
                    break

        self.map[h] = [key, value]
        self.size += 1

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, 
        or -1 if this map contains no mapping for the key.

        :type key: int
        :rtype: int
        """
        h = self._hash(key)

        while self.map[h][0] is not None:
            if self.map[h][0] == key:
                return self.map[h][1]
            else:
                h = self._rehash(h)

        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key 
        if this map contains a mapping for the key.
        
        :type key: int
        :rtype: None
        """
        h = self._hash(key)

        while self.map[h][0]:
            if self.map[h][0] == key:
                self.map[h] = [-1, None]
                self.size -= 1
                return None
            else:
                h = self._rehash(h)


def main():
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print hashMap.get(1)             # returns 1
    print hashMap.get(3)             # returns -1 (not found)
    hashMap.put(2, 1)                # update the existing value
    print hashMap.get(2)             # returns 1
    hashMap.remove(2)                # remove the mapping for 2
    print hashMap.get(2)             # returns -1 (not found)


if __name__ == '__main__':
    main()
