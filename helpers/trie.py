class TrieNode:

    def __init__(self, char):
        self.char = char
        self.end = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = TrieNode(char)
                node = node.children[char]

        node.end = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True
