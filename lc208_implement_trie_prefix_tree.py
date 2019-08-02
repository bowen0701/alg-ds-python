"""Leetcode 208. Implement Trie (Prefix Tree)
Medium

URL: https://leetcode.com/problems/implement-trie-prefix-tree/

Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.

Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
"""

class Node(object):
    def __init__(self):
        self.children = {}
        self.word = None


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None

        Time complexity: O(k), where k is the length of word.
        Space complexity: O(k).
        """
        current = self.root

        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                new = Node()
                current.children[c] = new
                current = new

        current.word = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool

        Time complexity: O(k), where k is the word length.
        Space complexity: O(1).
        """
        current = self.root

        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        if current.word == word:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool

        Time complexity: O(k), where k is the word prefix.
        Space complexity: O(1).
        """
        current = self.root

        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return False

        return True

def main():
    trie = Trie();
    trie.insert("apple")
    # Returns True.
    print trie.search("apple")
    # Returns False.
    print trie.search("app")
    # Returns True.
    print trie.startsWith("app")
    trie.insert("app")
    # Returns True.
    print trie.search("app")


if __name__ == '__main__':
    main()
