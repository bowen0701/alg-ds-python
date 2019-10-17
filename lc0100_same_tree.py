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

        Apply recursive preorder traversal to check same tree.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Check if both root don't exist.
        if not p and not q:
            return True

        # Check if just one of roots exits.
        if not p or not q:
            return False

        # If both exist, check their values are the same. 
        if p.val != q.val:
            return False

        # Recursively check left/right subtrees.
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


class SolutionPreorderIter(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool

        Apply iterative preorder traversal to check same tree.

        Time complexity: O(n).
        Space complexity: O(n).
        """
        stack = [(p, q)]

        while stack:
            cur_p, cur_q = stack.pop()

            # Check if both root don't exist, continue, 
            # since there may be other node pairs to check.
            if not cur_p and not cur_q:
                continue

            # Check if just one of roots exits.
            if not cur_p or not cur_q:
                return False

            # If both exist, check their values are the same. 
            if cur_p.val != cur_q.val:
                return False

            # Add root's right and then left to stack, since stack is FILO.
            stack.append((cur_p.right, cur_q.right))
            stack.append((cur_p.left, cur_q.left))

        return True


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
    print SolutionPreorderIter().isSameTree(p, q)

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
    print SolutionPreorderIter().isSameTree(p, q)

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
    print SolutionPreorderIter().isSameTree(p, q)

    # Input: [10,5,15], [10,5,null,null,15]
    p = TreeNode(10)
    p.left = TreeNode(5)
    p.right = TreeNode(15)
    q = TreeNode(10)
    q.left = TreeNode(5)
    q.left.right = TreeNode(15)
    print SolutionPreorderRecur().isSameTree(p, q)
    print SolutionPreorderIter().isSameTree(p, q)


if __name__ == '__main__':
    main()
