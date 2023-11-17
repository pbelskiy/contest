class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        h, w = len(mat), len(mat[0])

        answer = [[0]*w for _ in range(h)]

        for i in range(h):
            for j in range(w):
                for y in range(max(0, i - k), min(h, i + k + 1)):
                    for x in range(max(0, j - k), min(w, j + k + 1)):
                        answer[i][j] += mat[y][x]

        return answer
