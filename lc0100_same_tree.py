"""Leetcode 100. Same Tree
Easy

URL: https://leetcode.com/problems/same-tree/

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and
the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3
        [1,2,3],  [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2
        [1,2],    [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2
        [1,2,1],  [1,1,2]
Output: false
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPreorderRecur(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool

        Time complexity: O(n).
        Space complexity: O(n).
        """
        if not p or not q:
            return p is q
        
        return (p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


def main():
    # Input:     1         1
    #           / \       / \
    #          2   3     2   3
    #         [1,2,3],  [1,2,3]
    # Output: true
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print SolutionPreorderRecur().isSameTree(p, q)

    # Input:     1         1
    #           /           \
    #          2             2
    #         [1,2],    [1,null,2]
    # Output: false
    p = TreeNode(1)
    p.left = TreeNode(2)
    q = TreeNode(1)
    q.right = TreeNode(2)
    print SolutionPreorderRecur().isSameTree(p, q)    

    # Input:     1         1
    #           / \       / \
    #          2   1     1   2
    #         [1,2,1],  [1,1,2]
    # Output: false
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(1)
    q = TreeNode(1)
    q.left = TreeNode(1)
    q.right = TreeNode(2)
    print SolutionPreorderRecur().isSameTree(p, q)


if __name__ == '__main__':
    main()
