"""Leetcode 701. Insert into a Binary Search Tree
Medium

URL: https://leetcode.com/problems/insert-into-a-binary-search-tree/

Given the root node of a binary search tree (BST) and a value to be inserted 
into the tree, insert the value into the BST. Return the root node of the BST 
after the insertion. It is guaranteed that the new value does not exist in the
original BST.

Note that there may exist multiple valid ways for the insertion, as long as 
the tree remains a BST after insertion. You can return any of them.

For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:
         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionRecur(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        Time complexity: O(logn) for balanced tree; O(n) for single sided tree.
        Time complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        # Apply recursion to find the position to insert new node.
        new = TreeNode(val)

        if not root:
            return new

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


class SolutionIter(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        Time complexity: O(logn) for balanced tree; O(n) for single sided tree.
        Space complexity: O(1).
        """
        new = TreeNode(val)
        current = root

        while current:
            if val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = new
                    break
            else:
                if current.left:
                    current = current.left
                else:
                    current.left = new
                    break

        return root


def main():
    """
    Given the tree:
        4
       / \
      2   7
     / \
    1   3
    """
    bst_recur = TreeNode(4)
    bst_recur = SolutionRecur().insertIntoBST(bst_recur, 2)
    bst_recur = SolutionRecur().insertIntoBST(bst_recur, 7)
    bst_recur = SolutionRecur().insertIntoBST(bst_recur, 1)
    bst_recur = SolutionRecur().insertIntoBST(bst_recur, 3)
    print (bst_recur.val,
           bst_recur.left.val, bst_recur.right.val,
           bst_recur.left.left.val, bst_recur.left.right.val)

    bst_iter = TreeNode(4)
    bst_iter = SolutionIter().insertIntoBST(bst_iter, 2)
    bst_iter = SolutionIter().insertIntoBST(bst_iter, 7)
    bst_iter = SolutionIter().insertIntoBST(bst_iter, 1)
    bst_iter = SolutionIter().insertIntoBST(bst_iter, 3)
    print (bst_iter.val,
           bst_iter.left.val, bst_iter.right.val,
           bst_iter.left.left.val, bst_iter.left.right.val)

    """
    Insert: 5
         4
       /   \
      2     7
     / \   /
    1   3 5
    """
    bst_recur = SolutionIter().insertIntoBST(bst_recur, 5)
    print bst_recur.right.left.val

    bst_iter = SolutionIter().insertIntoBST(bst_iter, 5)
    print bst_iter.right.left.val


if __name__ == '__main__':
    main()
