"""Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given preorder and inorder traversal of a tree, construct the binary tree.

Note: You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionRecur(object):
    def _build(self, pre_start, pre_end, in_start, in_end,
               inorder_d, preorder, inorder):
        if pre_start > pre_end or in_start > in_end:
            return None

        # Preorder's first is root.
        root = TreeNode(preorder[pre_start])

        # Get root's pos in inorder.
        in_root_pos = inorder_d[root.val]

        # Compute the number of left from root.
        n_left = in_root_pos - in_start

        # Build binary trees for root's left and right.
        root.left = self._build(pre_start + 1, pre_start + n_left, 
                                in_start, in_root_pos - 1,
                                inorder_d, preorder, inorder)
        root.right = self._build(pre_start + n_left + 1, pre_end, 
                                 in_root_pos + 1, in_end,
                                 inorder_d, preorder, inorder)

        return root


    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # Create dict for inorder value->index.
        inorder_d = {v: i for (i, v) in enumerate(inorder)}

        # Build binary tree by recursion.
        return self._build(0, len(preorder) - 1, 0, len(inorder) - 1, 
                           inorder_d, preorder, inorder)


def main():
    # Ans:
    #   3
    #  / \
    # 9  20
    #   /  \
    #  15   7
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = SolutionRecur().buildTree(preorder, inorder)
    
    print root.val
    print root.left.val
    print root.right.val
    print root.right.left.val
    print root.right.right.val


if __name__ == '__main__':
    main()
