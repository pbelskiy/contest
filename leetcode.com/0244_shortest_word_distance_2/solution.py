class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)

        for i, w in enumerate(wordsDict):
            self.d[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        m = float('inf')

        for i in self.d[word1]:
            for j in self.d[word2]:
                m = min(m, abs(i - j))

        return m
