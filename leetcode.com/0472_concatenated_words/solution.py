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

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        sw = set(words)

        for w in words:
            trie.insert(w)

        def dfs(word, left, right):
            total = float('-inf')

            while right <= len(word):
                chunk = word[left:right]

                if not trie.startsWith(chunk):
                    break

                if chunk not in sw:
                    right += 1
                    continue

                # go deep
                total = max(total, dfs(word, right, right + 1) + 1)

                # continue search
                right += 1

            if left == len(word):
                return 0

            return total

        res = []
        for word in words:
            chunks = dfs(word, 0, 1)
            if chunks > 1:
                res.append(word)

        return sorted(res)
