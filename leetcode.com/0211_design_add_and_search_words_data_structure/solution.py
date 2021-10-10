class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.trie = Node('')

    def addWord(self, word: str) -> None:
        node = self.trie

        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                node.children[ch] = Node(ch)
                node = node.children[ch]

        node.end = True

    def search(self, word: str) -> bool:

        def dfs(node, p):
            if p == len(word):
                return node.end

            if word[p] in node.children:
                return dfs(node.children[word[p]], p + 1)

            if word[p] == '.':
                for child in node.children.values():
                    if dfs(child, p + 1):
                        return True

            return False

        return dfs(self.trie, 0)
