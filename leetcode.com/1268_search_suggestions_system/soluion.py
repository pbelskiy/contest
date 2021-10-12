class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node('')

    def add(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]

        node.end = True

    def dfs(self, node, prefix):
        if node.end:
            self.output.append(prefix + node.char)

        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def search(self, x):
        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        self.dfs(node, x[:-1])

        return sorted(self.output)


class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()

        for product in products:
            trie.add(product)

        suggestions = []

        for i in range(1, len(searchWord) + 1):
            suggestions.append(trie.search(searchWord[:i])[:3])

        return suggestions
