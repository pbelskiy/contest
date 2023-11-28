class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for row in mat:
            for i in range(len(row)):
                idx = (i + k) % len(row)
                if row[i] != row[idx]:
                    return False

        return True
