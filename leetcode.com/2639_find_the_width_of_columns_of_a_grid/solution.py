class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        a = list(zip(*grid[::-1]))
        r = []
        for col in a:
            m = 0
            for n in col:
                m = max(m, len(str(n)))

            r.append(m)

        return r
