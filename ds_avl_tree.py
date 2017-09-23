from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


def main():
    bst = AVLTree()
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
