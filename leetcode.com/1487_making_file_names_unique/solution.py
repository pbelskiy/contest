class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        d = {}

        for n in names:
            if n not in d:
                d[n] = True
                continue

            i = 1
            nn = f'{n}({i})'
            while nn in d:
                i += 1
                nn = f'{n}({i})'

            d[nn] = True

        return d.keys()
