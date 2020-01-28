"""Leetcode 211. Add and Search Word - Data structure design
Medium

URL: https://leetcode.com/problems/add-and-search-word-data-structure-design/

Design a data structure that supports the following two operations:
- void addWord(word)
- bool search(word)
search(word) can search a literal word or a regular expression string containing
only letters a-z or .. A . means it can represent any one letter.

Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
"""

class CharNode(object):
    def __init__(self):
        from collections import defaultdict

        # Create children dict: char->node.
        self.children = defaultdict()
        self.is_end = False


class WordDictionaryTrie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Apply Trie data structure.
        self.root = CharNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None

        Time complexity: O(n), where n is the length of word.
        Space complexity: O(n).
        """
        current = self.root

        # Iterate through word chars to add them to Trie.
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                current.children[c] = CharNode()
                current = current.children[c]

        current.is_end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. 
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool

        Time complexity: O(26^n).
        Space complexity: O(m), where m is the number of Trie nodes.
        """
        # Use stack to store (current node, partial word) for search.
        current = self.root
        stack = [(current, word)]

        while stack:
            cur, w = stack.pop()

            if w:
                # If word w exists, check if 1st char exists in its children.
                if w[0] in cur.children:
                    # If exists, add its child node and partial word to stack.
                    stack.append((cur.children[w[0]], w[1:]))
                elif w[0] == '.':
                    # If 1st char is '.', add all children nodes & partial word to stack.
                    for c_node in cur.children.values():
                        stack.append((c_node, w[1:]))
            else:
                # If w does not exist, arrived at the end of word. Check word match.
                if cur.is_end:
                    return True

        return False


def main():
    word_dict = WordDictionaryTrie()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    print word_dict.search("pad")  # false
    print word_dict.search("bad")  # true
    print word_dict.search(".ad")  # true
    print word_dict.search("b..")  # true


if __name__ == '__main__':
    main()
