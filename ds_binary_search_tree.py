from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class TreeNode(object):
    """Tree node class collects helper functions for BinarySearchTree."""
    def __init__(self, key, value, 
                 left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    # TODO: finish TreeNode class.


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


def main():
    bst = BinarySearchTree()
    pass


if __name__ == '__main__':
    main()
