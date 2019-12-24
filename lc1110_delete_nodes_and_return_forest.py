"""Leetcode 1110. Delete Nodes And Return Forest
Medium

URL: https://leetcode.com/problems/delete-nodes-and-return-forest/

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest
(a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the
result in any order.

Example 1:
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 
Constraints:
- The number of nodes in the given tree is at most 1000.
- Each node has a distinct value between 1 and 1000.
- to_delete.length <= 1000
- to_delete contains distinct values between 1 and 1000.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class SolutionHasParentPreorder(object):
    def _preorderRecur(self, root, has_parent, result, to_delete_set):
        # Base case.
        if not root:
            return None

        if root.val in to_delete_set:
            # If root is deleted, it left/right has no parent. Continue traversal.
            root.left = self._preorderRecur(root.left, False, result, to_delete_set)
            root.right = self._preorderRecur(root.right, False, result, to_delete_set)
            return None
        else:
            # If is not deleted and is root, collect it in result.
            if not has_parent:
                result.append(root)

            # Thus its left/right has parent. Continue traversal.
            root.left = self._preorderRecur(root.left, True, result, to_delete_set)
            root.right = self._preorderRecur(root.right, True, result, to_delete_set)
            return root

    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        # Use set for quick lookup.
        to_delete_set = set(to_delete)

        # Apply preorder traversal to collect forest trees's roots.
        result = []
        # Use has_parent to mark forest's tree root. False for main root.
        has_parent = False
        self._preorderRecur(root, has_parent, result, to_delete_set)
        return result


def main():
    # Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
    # Output: [[1,2,null,4],[6],[7]] => [1, 6, 7]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    to_delete = [3,5]
    forest_roots = SolutionHasParentPreorder().delNodes(root, to_delete)
    print [r.val for r in forest_roots]


if __name__ == '__main__':
    main()
