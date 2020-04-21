"""Leetcode 426. Convert Binary Search Tree to Sorted Doubly Linked List
Medium

URL: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and
successor pointers in a doubly-linked list. For a circular doubly linked list,
the predecessor of the first element is the last element, and the successor of
the last element is the first element.

We want to do the transformation in place. After the transformation, the left
pointer of the tree node should point to its predecessor, and the right pointer
should point to its successor. You should return the pointer to the smallest
element of the linked list.

Example 1:
Input: root = [4,2,5,1,3]
     4
    / \
   2   5
  / \
 1   3
Output: [1,2,3,4,5]
Explanation: The figure below shows the transformed BST. The solid line indicates
the successor relationship, while the dashed line means the predecessor relationship.

Example 2:
Input: root = [2,1,3]
Output: [1,2,3]

Example 3:
Input: root = []
Output: []
Explanation: Input is an empty tree. Output is also an empty Linked List.

Example 4:
Input: root = [1]
Output: [1]

Constraints:
- -1000 <= Node.val <= 1000
- Node.left.val < Node.val < Node.right.val
- All values of Node.val are unique.
- 0 <= Number of Nodes <= 2000
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionInorderIter(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node

        Time complexity: O(n).
        Space complexity: O(1).
        """
        # Apply iterative inorder traversal with stack for visited nodes.
        if not root:
            return None

        # Create pre_head for doubly linked list, and set it to previous.
        pre_head = Node(None)
        previous = pre_head
        current = root
        stack = []

        # Pop node from stack, connect parent and child nodes.
        while current or stack:
            # Visit the leftmost node.
            while current:
                stack.append(current)
                current = current.left

            # Pop stack's last node to get current.
            current = stack.pop()

            # Connect: previous <-> current.
            previous.right = current
            current.left = previous

            # Increment previous & current.
            previous = current
            current = current.right

        # Connect 1st (prev_head.right) and last nodes (previous).
        pre_head.right.left = previous
        previous.right = pre_head.right

        return pre_head.right


def main():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    dll_head = SolutionInorderIter().treeToDoublyList(root)
    print dll_head.val  # Output: 1.
    print dll_head.right.val  # Output: 2.
    print dll_head.right.right.val  # Output: 3.
    print dll_head.right.right.right.val  # Output: 4.
    print dll_head.right.right.right.right.val  # Output: 5.
    print dll_head.right.right.right.right.right.val  # Output: 1.
    print dll_head.left.val  # Output: 5.  


if __name__ == '__main__':
    main()
