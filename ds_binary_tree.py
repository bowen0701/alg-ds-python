from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class BinaryTree(object):
    """Binary Tree using class.

    Travesal:
    - Inorder (typical): left -> root -> right
    - Preorder: root -> left -> right
    - Postorder: left -> right -> root
    """
    def __init__(self, root):
        self.key = root
        self.left_tree = None
        self.right_tree = None

    def insert_left(self, new_node):
        if self.left_tree is None:
            self.left_tree = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_tree = self.left_tree
            self.left_tree = t

    def insert_right(self, new_node):
        if self.right_tree is None:
            self.right_tree = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_tree = self.right_tree
            self.right_tree = t

    def get_root_value(self):
        return self.key

    def set_root_value(self, new_value):
        self.key = new_value

    def get_left_tree(self):
        return self.left_tree

    def get_right_tree(self):
        return self.right_tree

    def __repr__(self):
        return '[{0}, {1}, {2}]'.format(
            self.key, self.left_tree, self.right_tree)


def preorder_travel(tree):
    if tree:
        print(tree.get_root_value())
        preorder_travel(tree.get_left_tree())
        preorder_travel(tree.get_right_tree())
    else:
        return None

def postorder_travel(tree):
    if tree is not None:
        postorder_travel(tree.get_left_tree())
        postorder_travel(tree.get_right_tree())
        print(tree.get_root_value())
    else:
        return None

def inorder_travel(tree):
    if tree is not None:
        inorder_travel(tree.get_left_tree())
        print(tree.get_root_value())
        inorder_travel(tree.get_right_tree())
    else:
        return None


def main():
    tree = BinaryTree(3)
    print('tree: {}'.format(tree.get_root_value()))

    tree.insert_left(4)
    print('tree.insert_left(4): {}'
          .format(tree.get_left_tree().get_root_value()))

    tree.insert_left(5)
    print('tree.insert_left(5): {}'
          .format(tree.get_left_tree().get_root_value()))

    tree.insert_right(6)
    print('tree.insert_right(6): {}'
          .format(tree.get_right_tree().get_root_value()))

    tree.insert_right(7)
    print('tree.insert_right(7): {}'
          .format(tree.get_right_tree().get_root_value()))

    left = tree.get_left_tree()
    print('left: {}'.format(left.get_root_value()))

    left.set_root_value(9)
    print('left.set_root_value(9): {}'
          .format(left.get_root_value()))

    left.insert_left(11)
    print('left.insert_left(11): {}'
          .format(left.get_left_tree().get_root_value()))

    print('Get right tree of right tree of tree:')
    print(tree.get_right_tree()
              .get_right_tree()
              .get_root_value())

    print('tree: {}'.format(tree))

    print('preorder_travel: ')
    print(preorder_travel(tree))

    print('postorder_travel: ')
    print(postorder_travel(tree))

    print('inorder_travel: ')
    print(inorder_travel(tree))


if __name__ == '__main__':
    main()
