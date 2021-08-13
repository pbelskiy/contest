class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        coordinates = set()

        m = len(matrix)
        n = len(matrix[0])

        # get
        for y in range(m):
            for x in range(n):
                if matrix[y][x] != 0:
                    continue

                for dx in range(0, n):
                    coordinates.add((y, dx))
                for dy in range(0, m):
                    coordinates.add((dy, x))

        # set
        for y, x in coordinates:
            matrix[y][x] = 0
