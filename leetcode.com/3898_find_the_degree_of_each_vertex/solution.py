class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        g = defaultdict(set)
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    g[i].add(j)
                    g[j].add(i)

        ans = []
        for i in range(n):
            ans.append(len(g[i]))

        return ans

