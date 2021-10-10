class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        l.sort(key=lambda k: int(k[-1]))
        return ' '.join(map(lambda t: t[:-1], l))
