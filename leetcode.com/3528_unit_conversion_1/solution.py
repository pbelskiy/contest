class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        conversions.sort()

        d = {0: 1}

        q = conversions
        while q:
            qq = []
            for a, b, f in q:
                if a in d:
                    d[b] = (d[a]*f) % (10**9 + 7)
                else:
                    qq.append((a, b, f))

            q = qq

        return [v for _, v in sorted(d.items())]

