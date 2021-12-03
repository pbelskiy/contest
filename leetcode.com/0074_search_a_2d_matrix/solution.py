class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h, w = len(matrix), len(matrix[0])
        left, right = 0, h*w

        while left < right:
            mid = (left + right) // 2

            y, x = mid // w, mid % w

            if matrix[y][x] == target:
                return True

            if matrix[y][x] > target:
                right = mid
            else:
                left = mid + 1

        return False
