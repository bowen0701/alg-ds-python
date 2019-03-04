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
    """Trie class.

    Operations:
      - insert()
      - search_prefix()
      - search_word()
      - delete()
      - start_with_prefix()
      - get_data()
    """
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

    def search_prefix(self, prefix):
        """Search a prefix.

        Time complexity: O(l), where l is average length of word.
        Space complexity: O(1).
        """
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return True

    def search_word(self, word):
        """Search a word.

        Time complexity: O(l), where l is average length of word.
        Space complexity: O(1).
        """
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        if node.word == word:
            return True
        else:
            return False


    def delete(self, word):
        """Delete a word.

        Time complexity: O(l*n), where l is average length of word, and 
          n is the number of words.        
        Space complexity: O(1).
        """
        previous = None
        node = self.root

        for char in word:
            if char in node.children:
                previous = node
                node = node.children[char]
            else:
                print('The word {} does not exist'.format(word))
                return None

        # TODO: Fix bug for delete redundant nodes.
        if node.children:
            node.data = None
            node.word = None
            return None
        else:
            for char in word[::-1]:
                print(char)
                if not node.children:
                    node = previous
                    node.children.pop(char)
                else:
                    break
     
    def start_with_prefix(self, prefix):
        """Get words starting with prefix."""
        pass

    def get_data(self, word):
        """Get word's data."""
        pass


def main():
    trie = Trie()

    trie.insert('abc', 1)
    print('{}'.format(trie.root
        .children['a'].children['b']
        .children['c'].word))

    trie.insert('abgl', 2)
    trie.insert('cdf', 3)
    trie.insert('abcd', 4)
    trie.insert('lmn', 5)
    print('Search word "abgl" (True): {}'.format(trie.search_word('abgl')))
    print('Search word "cdf" (True): {}'.format(trie.search_word('cdf')))
    print('Search word "abcd" (True): {}'.format(trie.search_word('abcd')))
    print('Search word "lmn" (True): {}'.format(trie.search_word('lmn')))

    print('Search prefix "ab" (True): {}'.format(trie.search_prefix('ab')))
    print('Search prefix "lo" (False)'.format(trie.search_prefix('lo')))

    print('Search word "lmn" (True): {}'.format(trie.search_word('lmn')))
    print('Search word "ab" (False): {}'.format(trie.search_word('ab')))
    print('Search word "cdf" (True): {}'.format(trie.search_word('cdf')))
    print('Search word "ghi" (False): {}'.format(trie.search_word('ghi')))

    print('Delete word "abc":')
    trie.delete('abc')
    print('Search word "abc" (False): {}'.format(trie.search_word('abc')))

    print('Delete word "abgl":')
    trie.delete('abgl')
    print('Search word "abgl" (False): {}'.format(trie.search_word('abgl')))

    print('Delete word "abcd":')
    trie.delete('abcd')
    print('Search word "abcd" (False): {}'.format(trie.search_word('abcd')))


if __name__ == '__main__':
    main()
