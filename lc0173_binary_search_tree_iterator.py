"""Leetcode 173. Binary Search Tree Iterator
Medium

URL: https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Example:
    7
   / \
  3  15
    /  \
   9   20  
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

Note:
- next() and hasNext() should run in average O(1) time and uses O(h) memory, 
  where h is the height of the tree.
- You may assume that next() call will always be valid, that is, there will be
  at least a next smallest number in the BST when next() is called.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BSTIteratorCurrentStackInorderIter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # Creat global previous/current and stack for collected sorted nodes.
        self.previous = None
        self.current = root
        self.stack = []

    def next(self):
        """
        @return the next smallest number
        :rtype: int

        Time complexity: O(1).
        Space complexity: O(h).
        """
        # Apply iterative inorder traversal with inside loop.
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

        current = self.stack.pop()

        self.previous = current
        self.current = current.right

        return current.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool

        Time complexity: O(1).
        Space complexity: O(h).
        """
        return bool(self.current or self.stack)


def main():
    #   7
    #  / \
    # 3  15
    #   /  \
    #  9   20
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)

    iterator = BSTIteratorCurrentStackInorderIter(root);
    print iterator.next()     # return 3
    print iterator.next()     # return 7
    print iterator.hasNext()  # return true
    print iterator.next()     # return 9
    print iterator.hasNext()  # return true
    print iterator.next()     # return 15
    print iterator.hasNext()  # return true
    print iterator.next()     # return 20
    print iterator.hasNext()  # return false


if __name__ == '__main__':
    main()
