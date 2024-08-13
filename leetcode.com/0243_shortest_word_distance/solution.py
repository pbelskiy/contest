class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1 = []
        i2 = []

        for i, w in enumerate(wordsDict):
            if w == word1:
                i1.append(i)
            elif w == word2:
                i2.append(i)

        m = float('inf')
        for i in range(len(i1)):
            for j in range(len(i2)):
                m = min(m, abs(i1[i] - i2[j]))

        return m
