class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end = False


class Solution:

    def __init__(self):
        self.trie = Node('')

    def add(self, word) -> None:
        node = self.trie

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = Node(char)
                node = node.children[char]

        node.end = True

    def dfs(self, board, node, y, x, path):
        h, w = len(board), len(board[0])

        if node.end:
            self.output.append(path)
            node.end = False

        if not (0 <= y < h and 0 <= x < w):
            return

        ch = board[y][x]

        if ch not in node.children:
            return

        board[y][x] = '#'

        for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            self.dfs(board, node.children[ch], cy, cx, path + ch)

        board[y][x] = ch

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.output = []

        for word in words:
            self.add(word)

        h, w = len(board), len(board[0])

        for y in range(h):
            for x in range(w):
                self.dfs(board, self.trie, y, x, '')

        return self.output
