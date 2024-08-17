class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        h, w = len(words), len(words[0])

        for i, word in enumerate(words):
            if len(word) != max(h, w):
                words[i] += ' '*(max(h, w) - len(words[i]))

        rm = list(zip(*words))
        for i, row in enumerate(rm):
            if words[i] != ''.join(row):
                return False

        return True
