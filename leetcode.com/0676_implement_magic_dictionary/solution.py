class Node:
    def __init__(self):
        self.children = {}
        self.end = False


class MagicDictionary:

    def __init__(self):
        self.root = Node()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = Node()
                node = node.children[char]
            node.end = True

    def get(self, node, word, remain):
        if remain < 0:
            return False

        if not word:
            return node.end and remain == 0

        for char in node.children.keys():
            if char == word[0]:
                if self.get(node.children[char], word[1:], remain):
                    return True
            elif remain == 1:
                if self.get(node.children[char], word[1:], 0):
                    return True
        return False

    def search(self, searchWord: str) -> bool:
        return self.get(self.root, searchWord, 1)
