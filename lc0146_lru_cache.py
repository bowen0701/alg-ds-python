"""Leetcode 146. LRU Cache
Medium

URL: https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.
- get(key) - Get the value (will always be positive) of the key if the key exists in
  the cache, otherwise return -1.
- put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used
item before inserting a new item.

The cache is initialized with a positive capacity.

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Follow up:
Could you do both operations in O(1) time complexity?

Your LRUCache object will be instantiated and called as such:
obj = LRUCache(capacity)
param_1 = obj.get(key)
obj.put(key, value)
"""

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """Least Recently Used (LRU) cache.

        Apply dict with a doubly linked list (head->tail) for LRU cache (old->new).

        :type capacity: int
        """
        self.capacity = capacity

        # Use a key_nodes dict to store key and its node with val.
        self.key_node_d = dict()

        # Initialize doubly linked list with linked head and tail.
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node_prev = node.prev
        node_next = node.next

        # Link node's prev and next together.
        node.prev.next = node_next
        node.next.prev = node_prev

    def _add_tail(self, node):
        # Get the recently used node.
        tail_prev = self.tail.prev

        # Link tail's prev and node together.
        tail_prev.next = node
        node.prev = tail_prev

        # Link node and tail together.
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(1).
        """
        # Check if key exists in dict, if yes, adjust key's pos.
        if key in self.key_node_d:
            node = self.key_node_d[key]

            # Remove node from doubly linked list, and then add it back to tail.
            self._remove(node)
            self._add_tail(node)

            # Return node's value.
            return node.value

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None

        Time complexity: O(1).
        Space complexity: O(1).
        """
        node = Node(key, value)

        # Check if the node with key exists, if yes, remove it.
        if key in self.key_node_d:
            self._remove(self.key_node_d[key])

        # Add new node to tail and update dict.
        self._add_tail(node)
        self.key_node_d[key] = node

        # Check if larger than capacity, remove head's next node: LRU node.
        if len(self.key_node_d) > self.capacity:
            head_next = self.head.next
            self._remove(head_next)
            del self.key_node_d[head_next.key]


def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print 'Returns 1:', cache.get(1)
    cache.put(3, 3)
    print 'Returns -1:', cache.get(2)
    cache.put(4, 4)
    print 'Returns -1:', cache.get(1)
    print 'Returns 3:', cache.get(3)
    print 'Returns 4:', cache.get(4)


if __name__ == '__main__':
    main()
