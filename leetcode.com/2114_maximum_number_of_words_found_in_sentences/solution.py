class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0

        for s in sentences:
            m = max(m, len(s.split(' ')))

        return m
