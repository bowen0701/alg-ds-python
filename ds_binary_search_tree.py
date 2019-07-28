from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
    """Node class collects helper functions for BinarySearchTree."""
    def __init__(self, key, data=None, left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree(object):
    """Binary search tree class.

    Property:
    - The left subtree of a node contains only nodes with keys lesser than 
      the node's key.
    - The right subtree of a node contains only nodes with keys greater than 
      the node's key.

    Travesal:
    - Inorder (typical): left -> root -> right
    - Preorder: root -> left -> right
    - Postorder: left -> right -> root
    """
    def __init__(self):
        self.root = None

    def search(self, node, key):
        """Search key starting from node.

        Time complexity: O(logh), where h is the height of node.
        Space complexity: O(1).
        """
        current = node
        while current and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current

    def find_minimum(self, node):
        """Find minimum starting from node.

        Time complexity: O(logh).
        Space complexity: O(1).
        """
        current = node
        while current.left:
            current = current.left
        return current

    def find_maximum(self, node):
        """Find maximum starting from node.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        current = node
        while current.right:
            current = current.right
        return current

    def find_successor(self, node):
        """Find succesor of node, i.e. next biggest node.

        Time complexity: O(logh).
        Space complexity: O(1).
        """
        current = node

        # If node's right existed, find leftmost node in node's right subtree.
        if current.right:
            return self.find_minimum(current.right)

        # If not, go up the tree to the lowest ancestor of node, 
        # whose "left" child is also an ancestor of node.
        parent = current.parent
        while parent and current == parent.right:
            current = parent
            parent = parent.parent
        return parent

    def find_predecessor(self, node):
        """Find predecessor of node, i.e. previous biggest node.

        Time complexity: O(logh).
        Space complexity: O(1).
        """
        current = node

        # If node's left existed, find rightmost node in node's left subtree.
        if current.left:
            return self.find_maximum(current.left)

        # If not, go up the tree to the lowest ancestor of node, 
        # whose "right" child is also an ancestor of node.
        parent = current.parent
        while parent and current == parent.left:
            current = parent
            parent = parent.parent
        return parent

    def insert(self, new_key, new_data=None):
        """Insert a new node with key.

        Use current and parent to track new node's insertion postion
        and its parent.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        new = Node(new_key, data=new_data)

        parent = None
        current = self.root

        # Go down to the bottom node whose parent will be new node's parent.
        while current:
            parent = current
            if new_key < current.key:
                current = current.left
            else:
                current = current.right
        new.parent = parent

        if not parent:
            # If the tree is empty.
            self.root = new
        elif new_key < parent.key:
            parent.left = new
        else:
            parent.right = new

    def _transplant(self, from_node, to_node):
        """Helper function for delete(): Transplant a subtree.
        
        Time complexity: O(1).
        Space complexity: O(1).
        """
        if not to_node.parent:
            self.root = from_node
        elif to_node == to_node.parent.left:
            # If to_node is its parent's left node.
            to_node.parent.left = from_node
        else:
            # If to_node is its parent's right node.
            to_node.parent.right = from_node

        if from_node:
            from_node.parent = to_node.parent

    def delete(self, del_node):
        """Delete node.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        if not del_node.left:
            # If node has no left child, transplant right subtree to it.
            self._transplant(del_node.right, del_node)
        elif not del_node.right:
            # If node has no right child, transplant left subtree to it.
            self._transplant(del_node.left, del_node)
        else:
            # Node has both left & right children.
            # Find its "lower" succesor which has no left child.
            trans_node = self.find_minimum(del_node.right)

            # If trans_node's parent is not del_node,
            # transplant its right node to it, and take over del_node's right. 
            if trans_node.parent != del_node:
                self._transplant(trans_node.right, trans_node)
                trans_node.right = del_node.right
                trans_node.right.parent = trans_node

            # Finally, transplant trans_node to del_node.
            self._transplant(trans_node, del_node)
            trans_node.left = del_node.left
            trans_node.left.parent = trans_node

    def inorder_traverse_recur(self, node):
        """Inorder walk: left -> root -> right.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if node:
            self.inorder_traverse_recur(node.left)
            print(node.key)
            self.inorder_traverse_recur(node.right)

    def preorder_traverse_recur(self, node):
        """Preorder walk: root -> left -> right.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if node:
            print(node.key)
            self.preorder_traverse_recur(node.left)
            self.preorder_traverse_recur(node.right)

    def postorder_traverse_recur(self, node):
        """Postorder walk: left -> right -> root.

        Time complexity: O(n).
        Space complexity: O(1).
        """
        if node:
            self.postorder_traverse_recur(node.left)
            self.postorder_traverse_recur(node.right)
            print(node.key)


def main():
    """
    Tree:
        6
       / \
      5   7
     / \   \
    2   5   8
    """
    bst = BinarySearchTree()
    bst.insert(6)
    bst.insert(5)
    bst.insert(7)
    bst.insert(2)
    bst.insert(5)
    bst.insert(8)

    # Inorder walk: 2, 5, 5, 6, 7, 8.
    print('Inorder walk:')
    bst.inorder_traverse_recur(bst.root)
    # Preorder walk: 6, 5, 2, 5, 7, 8.
    print('Preorder walk:')
    bst.preorder_traverse_recur(bst.root)
    # Postorder walk: 2, 5, 5, 8, 7, 6.
    print('Postorder walk:')
    bst.postorder_traverse_recur(bst.root)

    # Search existing key 6.
    print('Search existing node with key 6:')
    print(bst.search(bst.root, 6).key)
    # Search nonexisting key 10.
    print('Search nonexisting node with key 10:')
    print(bst.search(bst.root, 10))

    # Find min of root: 2.
    print('Find min: {}'.format(bst.find_minimum(bst.root).key))
    # Find min of root's right: 7.
    print('Find min from 7: {}'.format(bst.find_minimum(bst.root.right).key))

    # Find max of root: 2.
    print('Find max: {}'.format(bst.find_maximum(bst.root).key))
    # Find max of root's right: 8.
    print('Find max from 7: {}'.format(bst.find_maximum(bst.root.right).key))

    # Find successor of root: 7.
    print('Find successor: {}'.format(bst.find_successor(bst.root).key))
    # Find successor of root's left's right: 6.
    print('Find successor from second 5: {}'
          .format(bst.find_successor(bst.root.left.right).key))

    # Find predecessor of root: 6.
    print('Find predecessor: {}'.format(bst.find_predecessor(bst.root).key))
    # Find successor of root's left's right: 5.
    print('Find predecessor from 5: {}'
          .format(bst.find_predecessor(bst.root.left).key))

    # Delete root's left: 5, the run inorder walk: 2, 5, 6, 7, 8.
    bst.delete(bst.root.left)
    print('Inorder traversal:')
    bst.inorder_traverse_recur(bst.root)

    # Further delete root: 6, the run inorder walk: 2, 5, 7, 8.
    bst.delete(bst.root)
    print('Inorder walk:')
    bst.inorder_traverse_recur(bst.root)


if __name__ == '__main__':
    main()
