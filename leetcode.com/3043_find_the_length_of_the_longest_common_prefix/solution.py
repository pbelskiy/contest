class Node:

    def __init__(self, char: str) -> None:
        self.char = char
        self.children = {}


class Trie:

    def __init__(self) -> None:
        self.root = Node('')

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = Node(char)
                node = node.children[char]

    def get_longest_prefix(self, word: str) -> int:
        node = self.root
        length = 0

        for char in word:
            if char not in node.children:
                break

            node = node.children[char]
            length += 1

        return length


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for n in set(map(str, arr2)):
            trie.insert(n)

        m = 0
        for n1 in set(map(str, arr1)):
            m = max(m, trie.get_longest_prefix(n1))

        return m
