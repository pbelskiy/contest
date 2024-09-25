"""
Simple Trie with few tricks:

1) Save the counter of how many time we visit node
2) Don't brute force each prefix, just sum of all counts when path follow.
"""
class Node:
    def __init__(self) -> None:
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, s: str) -> None:
        node = self.root

        for ch in s:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
            node.count += 1

    def search(self, s: str) -> int:
        node = self.root
        count = 0

        for ch in s:
            if ch not in node.children:
                break

            node = node.children[ch]
            count += node.count

        return count


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for w in words:
            trie.insert(w)

        res = []
        for w in words:
            res.append(trie.search(w))

        return res
