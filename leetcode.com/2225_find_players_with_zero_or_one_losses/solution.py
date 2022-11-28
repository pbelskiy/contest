class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        a0, a1 = set(), set()

        d = Counter()
        for w, l in matches:
            d[l] += 1

        for w, l in matches:
            if w not in d:
                a0.add(w)
            if d[l] == 1:
                a1.add(l)

        return [sorted(a0), sorted(a1)]
