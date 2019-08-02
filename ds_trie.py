from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
    """Node class for Trie class."""
    def __init__(self):
        self.children = {}
        self.word = None


class Trie(object):
    """Trie class.

    Methods:
      - insert()
      - search()
      - delete()
      - search_prefix()
      - have_prefix()
    """
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """Insert a word.

        Time complexity: O(k), where k is the word length.
        Space complexity: O(k).
        """
        current = self.root

        # Go through each char in word, check it exists or not in children.
        # If char exist, visit it's child; if not, create child node.
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                new = Node()
                current.children[c] = new
                current = new

        current.word = word

    def search(self, word):
        """Search a word.

        Time complexity: O(k), where k is the word length.
        Space complexity: O(1).
        """
        current = self.root

        # Go through each char in word and check its existence in children.
        # Finally arrive at the word node.
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        # Check the word exists or not.
        if current.word == word:
            return True
        else:
            return False

    def delete(self, word):
        """Delete a word.

        Time complexity: O(k), where k is the word length.       
        Space complexity: O(k).
        """
        current = self.root

        # Use stack to track all visiting chars.
        stack = [current]

        # Go through each char in word and check its existence in children.
        # Finally arrive at the word node.
        for c in word:
            if c in current.children:
                current = current.children[c]
                stack.append(current)
            else:
                # The word does not exist.
                return None

        if current.children:
            # If word node has any children, just remove its payload.
            current.word = None
            return None
        else:
            # If no children, check char in reversed order.
            # Further, if char has no children, pop it from children dict.
            stack.pop()

            for c in word[::-1]:
                if not current.children:
                    # Backtrack to the previous char.
                    current = stack.pop()
                    current.children.pop(c)
                else:
                    break

    def search_prefix(self, prefix):
        """Search a prefix.

        Time complexity: O(k), where k is the prefix length.
        Space complexity: O(1).
        """
        current = self.root

        # Go through each char in prefix and check its existence in children.
        # Finally arrive at the prefix node.
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        return True

    def have_prefix(self, prefix):
        """Get words starting with prefix.

        Time complexity: O(l*m), where 
          - l is the average word lenght,
          - m is the average number of connected words for each word.
        Space complexity: O(l*m).
        """
        words = []
        current = self.root

        # Go through each char in prefix and check its existence in children.
        # Finally arrive at the prefix node.
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                # The prefix does not exits.
                return None
        
        # Check whether prefix is a word, if yes, append it first.
        if current.word:
            words.append(current.word)

        # Run BFS with queue to collect the following words with prefix.
        visit_queue = [current]

        while visit_queue:
            node = visit_queue.pop()
            for c, child_node in node.children.items():
                visit_queue.insert(0, child_node)
                if child_node.word:
                    words.append(child_node.word)

        return words


def main():
    trie = Trie()

    # Trie example: https://www.youtube.com/watch?v=AXjmTQ8LEoI
    trie.insert('abc')
    print('{}'.format(trie.root
        .children['a'].children['b']
        .children['c'].word))

    trie.insert('abgl')
    trie.insert('cdf')
    trie.insert('abcd')
    trie.insert('lmn')
    trie.insert('lmnz')

    print('Prefix "ab": {}'.format(trie.root
        .children['a'].children['b']
        .children.keys()))

    print('Search word "abgl" (True): {}'.format(trie.search('abgl')))
    print('Search word "cdf" (True): {}'.format(trie.search('cdf')))
    print('Search word "abcd" (True): {}'.format(trie.search('abcd')))
    print('Search word "lmn" (True): {}'.format(trie.search('lmn')))

    print('Search prefix "ab" (True): {}'.format(trie.search_prefix('ab')))
    print('Search prefix "lo" (False): {}'.format(trie.search_prefix('lo')))

    print('Start with prefix "ab": (abc, abgl, abcd): {}'
          .format(trie.have_prefix('ab')))
    print('Start with prefix "abc": (abc, abcd): {}'
          .format(trie.have_prefix('abc')))
    print('Start with prefix "cd": (cdf): {}'
          .format(trie.have_prefix('cd')))

    print('Search word "lmn" (True): {}'.format(trie.search('lmn')))
    print('Search word "ab" (False): {}'.format(trie.search('ab')))
    print('Search word "cdf" (True): {}'.format(trie.search('cdf')))
    print('Search word "ghi" (False): {}'.format(trie.search('ghi')))

    print('Delete word "abc":')
    trie.delete('abc')
    print('Search word "abc" (False): {}'.format(trie.search('abc')))
    print('Show keys with prefix "ab": {}'.format(
        trie.root
        .children['a'].children['b']
        .children.keys()))

    print('Delete word "abgl":')
    trie.delete('abgl')
    print('Search word "abgl" (False): {}'.format(trie.search('abgl')))
    print('Show children with prefix "ab": {}'.format(
        trie.root
        .children['a'].children['b']
        .children.keys()))
    print('Show children with prefix "abc": {}'.format(
        trie.root
        .children['a'].children['b']
        .children['c'].children.keys()))

    print('Delete word "abcd":')
    trie.delete('abcd')
    print('Search word "abcd" (False): {}'.format(trie.search('abcd')))
    print('Show root\'s children: {}'.format(trie.root.children.keys()))


if __name__ == '__main__':
    main()
