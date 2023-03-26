class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        def solve(i, seen):
            l, v = 0, {}
            while True:
                if i in seen:
                    break

                j = edges[i]
                if j == -1:
                    break

                if j in v:
                    return l - v[j], v

                v[j] = l
                i = j
                l += 1

            return -1, v

        m = -1
        seen = set()
        for i in range(len(edges)):
            r, v = solve(i, seen)
            seen |= set(v.keys())
            m = max(m, r)

        return m
