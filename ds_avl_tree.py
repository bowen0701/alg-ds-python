from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ds_binary_search_tree import TreeNode, BinarySearchTree


class AVLTreeNode(TreeNode):
    def __init__(self, *args, **kwargs):
        super(AVLTreeNode, self).__init__(*args, **kwargs)
        self.balance_factor = 0


class AVLTree(BinarySearchTree):
    TreeNode = AVLTreeNode

    pass


def main():
    avlt = AVLTree()
    avlt[3] = 'red'
    avlt[4] = 'blue'
    avlt[6] = 'yellow'
    avlt[2] = 'black'

    print('len(avlt): {}'.format(len(avlt)))
    print('avlt.size: {}'.format(avlt.size))

    print(avlt[6])
    print(avlt[2])

    print('Iterate by the inorder traversal algorithm:')
    for x in avlt:
        print(x)

    print('Remove avlt[2] and then put it back')
    del avlt[2]
    for x in avlt:
        print(x)
    avlt[2] = 'black'

    print('Remove avlt[6] and then put it back')
    del avlt[6]
    for x in avlt:
        print(x)
    avlt[6] = 'yellow'

    print('Remove avlt[4] and then put it back')
    del avlt[4]
    for x in avlt:
        print(x)
    avlt[4] = 'blue'

    print('Iterate after del avlt[3]:')
    del avlt[3]
    for x in avlt:
        print(x)


if __name__ == '__main__':
    main()
