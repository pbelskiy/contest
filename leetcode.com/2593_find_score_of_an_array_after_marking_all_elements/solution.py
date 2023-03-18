class Solution:
    def findScore(self, nums: List[int]) -> int:
        score, heap, marked = 0, [], set()

        for i, n in enumerate(nums):
            heappush(heap, (n, i))

        while heap:
            n, i = heappop(heap)
            if i in marked:
                continue

            score += n
            marked |= {i - 1, i + 1}

        return score
