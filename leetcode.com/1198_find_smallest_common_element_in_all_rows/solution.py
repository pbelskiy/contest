class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        s = set(mat[0])

        for row in mat:
            s &= set(row)

        return min(s, default=-1)
