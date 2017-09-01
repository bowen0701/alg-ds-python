from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class BinaryTree(oject):
    """Binary Tree using class."""
    def __init__(self, root):
        self.key = root
        self.left_tree = None
        self.right_tree = None

    def insert_left(self, new_node):
        if self.left_tree is None:
            self.left_tree = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left = self.left_tree
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

    def set_root_value(self):
        # TODO: here
        pass


def main():
    pass


if __name__ == '__main__':
    main()
