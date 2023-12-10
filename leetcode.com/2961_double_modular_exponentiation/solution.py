class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        indices = []

        for i, (a, b, c, m) in enumerate(variables):
            if ((a**b % 10)**c) % m == target:
                indices.append(i)

        return indices
