class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index, count = 0, 0

        for i, row in enumerate(mat):
            cnt = row.count(1)
            if cnt > count:
                index, count = i, cnt

        return [index, count]
