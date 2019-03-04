from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
    """Node class for Trie class."""
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.word = None
        self.children = {}


class Trie(object):
    """Trie class."""
    def __init__(self):
        self.root = Node()

    def insert(self, word, data):
        """Insert a word.

        Time complexity: O(l*n), where l is average length of word, and 
          n is the number of words.
        Space complexity: O(l).
        """
        node = self.root

        for char in word:
            if node.children.get(char):
                node = node.children[char]
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node

        node.data = data
        node.word = word

    def find(self, word):
        """Find a word.

        Time complexity: O(l), where l is average length of word.
        Space complexity: O(1).
        """
        pass

    def delete(self, word):
        """Delete a word.

        Time complexity: O(l*n), where l is average length of word, and 
          n is the number of words.        
        Space complexity: O(1).
        """
        pass



def main():
    trie = Trie()

    trie.insert('Bowen', 1)
    print('trie: {}'.format(trie.root
        .children['B'].children['o']
        .children['w'].children['e']
        .children['n'].word))


if __name__ == '__main__':
    main()
