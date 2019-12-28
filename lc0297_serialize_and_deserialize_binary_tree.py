"""Leetcode 297. Serialize and Deserialize Binary Tree
Hard

URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

Example:
You may serialize the following tree:
    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a
binary tree. You do not necessarily need to follow this format, so please be
creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your
serialize and deserialize algorithms should be stateless.

Your Codec object will be instantiated and called as such:
codec = Codec()
codec.deserialize(codec.serialize(root))
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class CodecPreorderRecur:
    def _serializePreorderRecur(self, root, vals):
        if root:
            vals.append(str(root.val))
            self._serializePreorderRecur(root.left, vals)
            self._serializePreorderRecur(root.right, vals)
        else:
            vals.append('#')

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str

        Time complexity: O(n).
        Space complexity: O(n).
        """
        # Apply preorder traversal to collect values and '#' for empty nodes.
        vals = []
        self._serializePreorderRecur(root, vals)

        # Separate nodes's values by ','.
        return ','.join(vals)

    def _deserializePreorderRecur(self, vals_queue):
        val_str = vals_queue.popleft()
        if val_str != '#':
            root = TreeNode(int(val_str))
            root.left = self._deserializePreorderRecur(vals_queue)
            root.right = self._deserializePreorderRecur(vals_queue)
            return root
        else:
            return None

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode

        Time complexity: O(n).
        Space complexity: O(n).
        """
        from collections import deque

        vals = data.split(',')
        vals_queue = deque(vals)
        return self._deserializePreorderRecur(vals_queue)


def main():
    # Binary tree:
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5
    # Serialized: "1,2,#,#,3,4,#,#,5,#,#".
    # Deserialized: original binary tree.
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = CodecPreorderRecur()
    data = codec.serialize(root)
    print data
    deserialized_root = codec.deserialize(data)
    print deserialized_root.val                # 1
    print deserialized_root.left.val           # 2
    print deserialized_root.left.left          # None
    print deserialized_root.left.right         # None
    print deserialized_root.right.val          # 3
    print deserialized_root.right.left.val     # 4
    print deserialized_root.right.right.val    # 5
    print deserialized_root.right.left.left    # None
    print deserialized_root.right.left.right   # None
    print deserialized_root.right.right.left   # None
    print deserialized_root.right.right.right  # None


if __name__ == '__main__':
    main()
