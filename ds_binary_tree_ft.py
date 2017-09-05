from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def binary_tree(root):
    """Binary tree using list of list."""
    return [root, [], []]


def insert_left(root, new_branch):
    left_tree = root.pop(1)
    if len(left_tree) > 1:
        root.insert(1, [new_branch, left_tree, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    right_tree = root.pop(2)
    if len(right_tree) > 1:
        root.insert(2, [new_branch, [], right_tree])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_value(root):
    return root[0]

def set_root_value(root, new_val):
    root[0] = new_val

def get_left_tree(root):
    return root[1]

def get_right_tree(root):
    return root[2]


def preorder_travel(root):
    pass

def inorder_travel(root):
    pass

def postorder_travel(root):
    pass


def main():
    root = binary_tree(3)
    print('root: {}'.format(root))

    insert_left(root, 4)
    print('insert_left(root, 4): {}'.format(root))

    insert_left(root, 5)
    print('insert_left(root, 5): {}'.format(root))

    insert_right(root, 6)
    print('insert_right(root, 6): {}'.format(root))

    insert_right(root, 7)
    print('insert_right(root, 7): {}'.format(root))

    left = get_left_tree(root)
    print('get_left_tree(root): {}'.format(left))

    set_root_value(left, 9)
    print('set_root_value(left, 9): {}'.format(left))
    print('root: {}'.format(root))

    insert_left(left, 11)
    print('insert_left(left, 11): {}'.format(left))
    print('root: {}'.format(root))

    print('Get right tree of right tree:')
    print(get_right_tree(get_right_tree(root)))


if __name__ == '__main__':
    main()
