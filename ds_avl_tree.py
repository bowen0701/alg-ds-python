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

    def update_balance(self, node):
        if self.balance_factor < -1 or self.balance_factor > 1:
            self.rebalance(node)
            return None
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            else:
                pass

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def _put(self, key, value, current_node):
        if key == current_node.key:
            self.replace_node_data(
                key, value, current_node.left_child, current_node.right_child)
        elif key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, value, parent=current_node)
                self.update_balance(current_node.right_child)

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
