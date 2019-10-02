"""Leetcode 700. Search in a Binary Search Tree
Easy

URL: https://leetcode.com/problems/search-in-a-binary-search-tree/

Given the root node of a binary search tree (BST) and a value.
You need to find the node in the BST that the node's value equals the given value.
Return the subtree rooted with that node. 
If such node doesn't exist, you should return NULL.

For example, 
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to search: 2
You should return this subtree:
      2     
     / \   
    1   3
In the example above, if we want to search the value 5, since there is no node
with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the
expected output (serialized tree format) as [], not null.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        Time complexity: O(logn).
        Space complexity: O(logn), since stack calls.
        """
        if not root:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


class SolutionIter(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        if not root:
            return None

        current = root
        while current:
            if current.val == val:
                return current

            if val < current.val:
                current = current.left
            else:
                current = current.right

        return None


def main():
    # Given the tree:
    #         4
    #        / \
    #       2   7
    #      / \
    #     1   3
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # Output: 2
    val = 2
    print SolutionRecur().searchBST(root, val).val
    print SolutionIter().searchBST(root, val).val

    # Output: None
    val = 5
    print SolutionRecur().searchBST(root, val)
    print SolutionIter().searchBST(root, val)


if __name__ == '__main__':
    main()
