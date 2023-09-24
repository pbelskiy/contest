"""
Just build reversed Pascals's triangle.

TC: O(R), where R is queried row.
SC: O(R), where R is queried row.
"""
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev = [poured]

        for i in range(query_row + 1):
            if i == query_row:
                return min(1, prev[query_glass])

            curr = [0]*(len(prev) + 1)
            for j in range(len(prev)):
                if prev[j] > 1:
                    curr[j] += (prev[j] - 1) / 2
                    curr[j + 1] += (prev[j] - 1) / 2

            prev = curr

        return float('inf')
