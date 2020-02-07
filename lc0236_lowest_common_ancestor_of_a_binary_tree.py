"""Leetcode 236. Lowest Common Ancestor of a Binary Tree
Medium

URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendant of itself)."

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
      3
    /   \
   5     1
  / \   / \
 6   2 0   8
    / \
   7   4

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Note:
- All of the nodes' values will be unique.
- p and q are different and both values will exist in the binary tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionPreorderRecur(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for singly-linked list.
        """
        # Apply recursive Preorder Traversal: root->left->right.
        if not root:
            return None

        # Vist root: if root is p or q, we found p or q is LCA.
        if root is p or root is q:
            return root

        # Visit left & right recursively in left and right subtrees.
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # p & q are not in both subtrees.
        if not left and not right:
            return None

        # p and q are in left and right subtrees.
        if left and right:
            return root

        # Otherwise, p or q is in subtree.
        return left or right


class SolutionChildParentDictPreorderIter(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for singly-linked list.
        """
        # Use dict: child->parent.
        child_parent_d = {}
        child_parent_d[root] = None

        # Apply iterative preorder traversal to find p & q's parents.
        stack = [root]
        while p not in child_parent_d or q not in child_parent_d:
            current = stack.pop()

            # Visit right and then left since we use stack with FILO.
            if current.right:
                child_parent_d[current.right] = current
                stack.append(current.right)
            if current.left:
                child_parent_d[current.left] = current
                stack.append(current.left)

        # Use set to reversely collect p's ancestors.
        ancestors = set()
        while p:
            ancestors.add(p)
            p = child_parent_d[p]

        # Then reversely traverse q's parents until meet one of p's parents.
        while q not in ancestors:
            q = child_parent_d[q]

        return q


def main():
    import time

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    # Output: 3
    p = root.left
    q = root.right

    start_time = time.time()
    print SolutionPreorderRecur().lowestCommonAncestor(root, p, q).val
    print 'Time for recur: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionChildParentDictPreorderIter().lowestCommonAncestor(root, p, q).val
    print 'Time for iter: {}'.format(time.time() - start_time)

    # Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    # Output: 5
    p = root.left
    q = root.left.right.right

    start_time = time.time()
    print SolutionPreorderRecur().lowestCommonAncestor(root, p, q).val
    print 'Time for recur: {}'.format(time.time() - start_time)

    start_time = time.time()
    print SolutionChildParentDictPreorderIter().lowestCommonAncestor(root, p, q).val
    print 'Time for iter: {}'.format(time.time() - start_time)


if __name__ == '__main__':
    main()
