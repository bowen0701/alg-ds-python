"""Leetcode 617. Merge Two Binary Trees
Easy

URL: https://leetcode.com/problems/merge-two-binary-trees/

Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes
overlap, then sum node values up as the new value of the merged node. Otherwise,
the NOT null node will be used as the node of new tree.

Example 1:
Input: 
    Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output:
Merged tree:
         3
        / \
       4   5
      / \   \ 
     5   4   7

Note: The merging process must start from the root nodes of both trees.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPreorderRecur(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode

        Time complexity: O(n1+n2).
        Space complexity: O(logn1+logn2) for balanced tree; O(n1+n2) for single-sided.
        """
        # Apply recursive preorder traversal.
        if not t1 and not t2:
            return None

        if t1 and t2:
            root = TreeNode(t1.val + t2.val)

            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)

            return root
        else:
            return t1 or t2


def main():
    # Input: 
    #     Tree 1                     Tree 2                  
    #           1                         2                             
    #          / \                       / \                            
    #         3   2                     1   3                        
    #        /                           \   \                      
    #       5                             4   7                  
    # Output:
    # Merged tree:
    #          3
    #         / \
    #        4   5
    #       / \   \ 
    #      5   4   7
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    t = SolutionPreorderRecur().mergeTrees(t1, t2)
    print t.val              # Should be 3
    print t.left.val         # Should be 4
    print t.right.val        # Should be 5
    print t.left.left.val    # Should be 5
    print t.left.right.val   # Should be 4
    print t.right.right.val  # Should be 7


if __name__ == '__main__':
    main()
