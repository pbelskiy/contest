"""
Simple Trie as in the same medium problem, except two tricks:

1. Just reverse words to use trie (prefix -> suffix)
2. Update best index for node each time we add new word

TC: O(N*L+Q*L)
SC: O(N*L)
"""
class Node:
    def __init__(self, char: str, index: int) -> None:
        self.char = char
        self.children = {}
        self.index = index


class Trie:
    def __init__(self, words: List[str]) -> None:
        index = -1
        prev = float('inf')

        for i, w in enumerate(words):
            if len(w) < prev:
                prev = len(w)
                index = i

        self.root = Node('', index)
        self.words = words

    def _get_better(self, i, j):
        if len(self.words[i]) == len(self.words[j]):
            return i if i < j else j

        return i if len(self.words[i]) < len(self.words[j]) else j

    def insert(self, word: str, index: int) -> None:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
                node.index = self._get_better(node.index, index)
            else:
                node.children[char] = Node(char, index)
                node = node.children[char]

    def search(self, word: str) -> int:
        node = self.root

        for char in word:
            if char not in node.children:
                break

            node = node.children[char]

        return node.index


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie(wordsContainer)
        for i, w in enumerate(wordsContainer):
            trie.insert(w[::-1], i)

        res = []
        for w in wordsQuery:
            res.append(trie.search(w[::-1]))

        return res
