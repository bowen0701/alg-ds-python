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


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
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
    bst = TreeNode(4)
    bst = Solution().insertIntoBST(bst, 2)
    bst = Solution().insertIntoBST(bst, 7)
    bst = Solution().insertIntoBST(bst, 1)
    bst = Solution().insertIntoBST(bst, 3)

    print bst.val
    print bst.left.val
    print bst.right.val
    print bst.left.left.val
    print bst.left.right.val

    """
    Insert: 5
         4
       /   \
      2     7
     / \   /
    1   3 5
    """
    bst = Solution().insertIntoBST(bst, 5)
    print bst.right.left.val


if __name__ == '__main__':
    main()
