
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        def dfs(a, t, m):
            if t > k:
                return False
            if a == n - 1:
                return True

            for b, c in g[a]:
                if c >= m:
                    if dfs(b, t + c, m):
                        return True
            return False

        g = defaultdict(list)
        weights = set()
        n = len(online)

        for a, b, c in edges:
            if online[a] and online[b]:
                g[a].append((b, c))
                weights.add(c)

        weights = sorted(weights)

        # binary search on answer
        left, right = 0, len(weights) - 1
        r = -1

        while left <= right:
            mid = (left + right) // 2
            m = weights[mid]

            if dfs(0, 0, m):
                r = m
                left = mid + 1
            else:
                right = mid - 1

        return r

