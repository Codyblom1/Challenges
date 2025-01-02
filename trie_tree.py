"""
say we have a need to be predictive in finishing a word. We are given a prefix.
We need to be able to find all of the possible matches. Here we use a Trie tree creating it with two classes.
"""
class TrieNode:
    def __init(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # insert
    def insert(self, word):
        node = self.root
        for char in word:  # looping through the characters of the word
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True # marks the end of the word

    # Search for a word or prefix in the trie
    def search(self, prefix):
        node = self.root
        for char in prefix:  # Loop through each character in the prefix
            if char not in node.children:
                return None  # Prefix not found
            node = node.children[char]
        return node  # Return the node representing the prefix

    # Find all words starting with a prefix
    def starts_with(self, prefix):
        node = self.search(prefix)
        if not node:
            return []  # No words found
        return self._collect_words(node, prefix)

    # Helper method to collect all words from a given node
    def _collect_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)  # Add the word if this node is the end of a word
        for char, child in node.children.items():
            words.extend(self._collect_words(child, prefix + char))  # Recursively collect words
        return words
