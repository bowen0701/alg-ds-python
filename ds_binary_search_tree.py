from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class TreeNode(object):
    """Tree node class collects helper functions for BinarySearchTree."""
    def __init__(self, key, value, 
                 left=None, right=None, parent=None):
        self.key = key
        self.payload = value
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

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def __iter__(self):
        # Inorder traversal algorithm.
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


class BinarySearchTree(object):
    """Binary search tree class."""
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def _put(self, key, value, current_node):
        if key == current_node.key:
            self.replace_node_data(
                key, value, current_node.left_child, current_node.right_child)
        elif key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(
                    key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(
                    key, value, parent=current_node)

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def __setitem__(self, k, v):
        self.put(k, v)

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def remove(self, current_node):
        if current_node.is_leaf():
            # Leaf node.
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():
            # Interior node.
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:  
            # This node has one child.
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(
                        current_node.left_child.key,
                        current_node.left_child.payload,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(
                        current_node.right_child.key,
                        current_node.right_child.payload,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error: key not in tree.')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error: key not in tree.')

    def __delitem__(self, key):
        self.delete(key)


def main():
    bst = BinarySearchTree()
    bst[3] = 'red'
    bst[4] = 'blue'
    bst[6] = 'yellow'
    bst[2] = 'black'

    print('len(bst): {}'.format(len(bst)))
    print('bst.size: {}'.format(bst.size))

    print(bst[6])
    print(bst[2])

    print('Iterate by the inorder traversal algorithm:')
    for x in bst:
        print(x)

    print('Remove bst[2] and then put it back')
    del bst[2]
    for x in bst:
        print(x)
    bst[2] = 'black'

    print('Remove bst[6] and then put it back')
    del bst[6]
    for x in bst:
        print(x)
    bst[6] = 'yellow'

    print('Remove bst[4] and then put it back')
    del bst[4]
    for x in bst:
        print(x)
    bst[4] = 'blue'

    print('Iterate after del bst[3]:')
    del bst[3]
    for x in bst:
        print(x)


if __name__ == '__main__':
    main()
