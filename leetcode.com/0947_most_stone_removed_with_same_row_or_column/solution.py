class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def dfs(cx, cy):
            visited.add((cx, cy))

            for x, y in stones:
                if (x, y) in visited:
                    continue

                if cx == x or cy == y:
                    dfs(x, y)

        groups, visited = 0, set()

        for x, y in stones:
            if (x, y) not in visited:
                dfs(x, y)
                groups += 1

        return len(stones) - groups
