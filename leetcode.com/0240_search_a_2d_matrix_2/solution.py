class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target:
                break
            if row[-1] < target:
                continue

            i = bisect.bisect_right(row, target) - 1
            if row[i] == target:
                return True

        return False
