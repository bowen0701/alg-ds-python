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


class SolutionPreorderFirstInorderRootRecur(object):
    def _build(self, pre_start, pre_end, in_start, in_end,
               in_val_pos, preorder, inorder):
        if pre_start > pre_end or in_start > in_end:
            return None

        # Preorder's first is root.
        root = TreeNode(preorder[pre_start])

        # In inorder, get root's pos for separating left and right.
        in_root_pos = in_val_pos[root.val]

        # Compute the number of left from root.
        in_n_left = in_root_pos - in_start

        # Build binary trees from root's left and right.
        root.left = self._build(pre_start + 1, pre_start + in_n_left, 
                                in_start, in_root_pos - 1,
                                in_val_pos, preorder, inorder)
        root.right = self._build(pre_start + in_n_left + 1, pre_end, 
                                 in_root_pos + 1, in_end,
                                 in_val_pos, preorder, inorder)

        return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode

        - Preorder's first is root
        - In inorder, get root's position.
        - Then we can separate the the remaining data into left and right.
          preorder = [3,9,20,15,7]
                      ^ l r  r  r
          inorder  = [9,3,15,20,7]
                      l ^ r  r  r

        Time complexity: O(n), where n is the number of nodes.
        Space complexity: O(n).
        """
        # Create dict for inorder node->pos.
        in_val_pos = {v: i for (i, v) in enumerate(inorder)}

        # Build binary tree by recursion.
        pre_start, pre_end = 0, len(preorder) - 1
        in_start, in_end = 0, len(inorder) - 1
        return self._build(pre_start, pre_end, in_start, in_end,
                           in_val_pos, preorder, inorder)


def main():
    # Output: [3, 9, 20, 15, 7]
    #   3
    #  / \
    # 9  20
    #   /  \
    #  15   7
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = SolutionPreorderFirstInorderRootRecur().buildTree(preorder, inorder)
    
    print (root.val,
           root.left.val, root.right.val,
           root.right.left.val, root.right.right.val)


if __name__ == '__main__':
    main()
