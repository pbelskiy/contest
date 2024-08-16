class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = []

        for i in range(len(arrays)):
            m.append([arrays[i][-1], i])

        m.sort(reverse=True)
        best = 0

        for i in range(len(arrays)):
            v = arrays[i][0]
            for j in range(len(m)):
                if m[j][1] == i:
                    continue

                d = m[j][0] - v
                best = max(best, d)
                break

        return best
