class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = []
        for row in nums:
            h = []
            for n in row:
                heapq.heappush(h, -n)
            rows.append(h)

        score = 0
        while rows[0]:
            m = float('-inf')
            for row in rows:
                n = -heapq.heappop(row)
                m = max(m, n)

            score += m

        return score
