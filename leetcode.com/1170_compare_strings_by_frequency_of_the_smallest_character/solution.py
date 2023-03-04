class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        @cache
        def f(s):
            return Counter(s)[min(s)]

        res = []
        for q in queries:
            t = 0
            a = f(q)
            for w in words:
                if a < f(w):
                    t += 1
            res.append(t)

        return res
