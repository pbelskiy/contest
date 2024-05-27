class Solution:
    def compressedString(self, word: str) -> str:
        comp = ''

        i = 0
        s = 0
        while i < len(word):
            j = i + 1
            while j < len(word) and j - i < 9 and word[j] == word[i]:
                j += 1

            comp += str(j - i) + word[i]
            i = j

        return comp
