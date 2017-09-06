from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def binary_tree(tree):
    """Binary tree using list of list."""
    return [tree, [], []]


def insert_left(tree, new_branch):
    left_tree = tree.pop(1)
    if len(left_tree) > 1:
        tree.insert(1, [new_branch, left_tree, []])
    else:
        tree.insert(1, [new_branch, [], []])
    return tree

def insert_right(tree, new_branch):
    right_tree = tree.pop(2)
    if len(right_tree) > 1:
        tree.insert(2, [new_branch, [], right_tree])
    else:
        tree.insert(2, [new_branch, [], []])
    return tree


def get_root_value(tree):
    return tree[0]

def set_root_value(tree, new_val):
    tree[0] = new_val

def get_left_tree(tree):
    return tree[1]

def get_right_tree(tree):
    return tree[2]


def preorder_travel(tree):
    pass

def inorder_travel(tree):
    pass

def postorder_travel(tree):
    pass


def main():
    tree = binary_tree(3)
    print('tree: {}'.format(tree))

    insert_left(tree, 4)
    print('insert_left(tree, 4): {}'.format(tree))

    insert_left(tree, 5)
    print('insert_left(root, 5): {}'.format(tree))

    insert_right(tree, 6)
    print('insert_right(tree, 6): {}'.format(tree))

    insert_right(tree, 7)
    print('insert_right(tree, 7): {}'.format(tree))

    left = get_left_tree(tree)
    print('get_left_tree(tree): {}'.format(left))

    set_root_value(left, 9)
    print('set_root_value(left, 9): {}'.format(left))
    print('tree: {}'.format(tree))

    insert_left(left, 11)
    print('insert_left(left, 11): {}'.format(left))
    print('tree: {}'.format(tree))

    print('Get right tree of right tree:')
    print(get_right_tree(get_right_tree(tree)))


if __name__ == '__main__':
    main()
