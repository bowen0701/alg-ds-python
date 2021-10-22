"""Leetcode 572. Subtree of Another Tree
Easy

URL: https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure 
and node values with a subtree of s. 
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreorderSubtreeTreeMatchRecur:
    def _isTreeMatch(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case.
        if not root or not subRoot:
            return root is subRoot

        # Preorder traversal: root->left->right, to check root and left/right tree matches.
        if root.val != subRoot.val:
            return False

        return (self._isTreeMatch(root.left, subRoot.left)
                and self._isTreeMatch(root.right, subRoot.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(|s|*|t|), where |s| is the number of nodes in s.
        Space complexity: O(log|s|+log|t|), for balanced tree; 
          O(|s|+|t|) for single sided tree.
        """
        # Base case.
        if not root:
            return False

        # Check tree match first: if yes return True, if not, start checking left/right subtrees.
        # Preorder traversal: root->left->right, check if matches or subtree of left or right.
        if self._isTreeMatch(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot))


class SolutionTreeSerializationSubstringSearchBruteForce:
    def _serialize(self, root: Optional[TreeNode], root_chars: List[Optional[int]]) -> None:
        # Base cases.
        if not root:
            root_chars.append('#')
            return None

        # Apply preorder traversal: root->left->right, to serialize tree.
        root_chars.append(str(root.val))
        self._serialize(root.left, root_chars)
        self._serialize(root.right, root_chars)

    def _substring_search(self, root_chars: List[str], sub_root_chars: List[str]) -> bool:
        len_root = len(root_chars)
        len_sub_root = len(sub_root_chars)

        for i in range(len_root - len_sub_root):
            for j in range(len_sub_root):
                if root_chars[i + j] != sub_root_chars[j]:
                    break
                if j == len_sub_root - 1:
                    return i
        return len_root

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity: O(m*n + m + n) = O(m*n)
        Space complexity: O(m + n)
        """
        # Edge cases.
        if not root:
            return False

        # Apply preorder traversal for tree & subTree serialization.
        root_chars = []
        self._serialize(root, root_chars)

        sub_root_chars = []
        self._serialize(subRoot, sub_root_chars)

        # Apply substring search brute force algorithm.
        result = self._substring_search(root_chars, sub_root_chars)
        if result == len(root_chars):
            return False
        else:
            return True


class SolutionTreeSerializationSubstringSearchKmp:
    def serialize(self, root: Optional[TreeNode], root_vals: List[Optional[int]]) -> None:
        # Base cases.
        if not root:
            root_vals.append(None)
            return None

        # Apply preorder traversal: root->left->right, to serialize tree.
        root_vals.append(root.val)
        self.serialize(root.left, root_vals)
        self.serialize(root.right, root_vals)

    def KMP(self, root_str: str, sub_root_str: str) -> bool:
        pass

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity
        Space complexity
        """
        # Edge cases.
        if not root:
            return False

        # Apply preorder traversal for tree serialization.
        root_vals = []
        self.serialize(root, root_vals)
        print(f"root_vals: {root_vals}")

        sub_root_vals = []
        self.serialize(subRoot, sub_root_vals)
        print(f"sub_root_vals: {sub_root_vals}")

        # Apply KMP algorithm for string matching.
        return self.KMP(root_vals, sub_root_vals)


def main():
    # Given tree s:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    # Given tree t:
    #    4 
    #   / \
    #  1   2
    # Output: True
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(SolutionPreorderSubtreeTreeMatchRecur().isSubtree(root, subRoot))
    print(SolutionTreeSerializationSubstringSearchBruteForce().isSubtree(root, subRoot))
    # print(SolutionTreeSerializationStringSearchKmp().isSubtree(root, subRoot))

    # Given tree s:
    #      3
    #     / \
    #    4   5
    #   / \
    #  1   2
    #     /
    #    0
    # Given tree t:
    #    4
    #   / \
    #  1   2
    # Output: False
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)
    subRoot = TreeNode(4)
    subRoot.left = TreeNode(1)
    subRoot.right = TreeNode(2)
    print(SolutionPreorderSubtreeTreeMatchRecur().isSubtree(root, subRoot))
    print(SolutionTreeSerializationSubstringSearchBruteForce().isSubtree(root, subRoot))
    # print(SolutionTreeSerializationStringSearchKmp().isSubtree(root, subRoot))


if __name__ == '__main__':
    main()
