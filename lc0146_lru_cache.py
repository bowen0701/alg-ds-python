"""Leetcode 146. LRU Cache
Medium

URL: https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.

Implement the LRUCache class:
- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise
  return -1.
- void put(int key, int value) Update the value of the key if the key exists.
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds
  the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Example 1:
Input:
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output:
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);     // return 1
lRUCache.put(3, 3);  // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);     // returns -1 (not found)
lRUCache.put(4, 4);  // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);     // return -1 (not found)
lRUCache.get(3);     // return 3
lRUCache.get(4);     // return 4

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        """Least Recently Used (LRU) cache.

        Apply dict:key->node with a doubly linked list:
        head<->node1<->node2<->tail.

        :type capacity: int
        """
        self.capacity = capacity

        # Create a dict key_node_d: key->node.
        self.key_node_d = dict()

        # Create doubly linked list with head and tail.
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node_prev = node.prev
        node_next = node.next

        # Skip-connect node from prev and next.
        node.prev.next = node_next
        node.next.prev = node_prev

    def _add_tail(self, node):
        # Get the recently used node: tail_prev
        tail_prev = self.tail.prev

        # Connect tail's prev and node.
        tail_prev.next = node
        node.prev = tail_prev

        # Connect node and tail together.
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(1).
        """
        # Check if key exists in dict. If yes, adjust key's pos.
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

        # Check if node with key exists. If yes, remove it and update dict.
        if key in self.key_node_d:
            self._remove(self.key_node_d[key])
        self.key_node_d[key] = node

        # Add new node to tail.
        self._add_tail(node)

        # Check if larger than capacity, remove LRU node: head_next.
        if len(self.key_node_d) > self.capacity:
            head_next = self.head.next
            self._remove(head_next)
            del self.key_node_d[head_next.key]


def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print('Returns 1:', cache.get(1))
    cache.put(3, 3)
    print('Returns -1:', cache.get(2))
    cache.put(4, 4)
    print('Returns -1:', cache.get(1))
    print('Returns 3:', cache.get(3))
    print('Returns 4:', cache.get(4))


if __name__ == '__main__':
    main()
