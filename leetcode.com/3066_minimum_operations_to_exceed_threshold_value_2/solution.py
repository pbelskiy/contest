class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ops = 0

        while len(nums) >= 2:
            x, y = heappop(nums), heappop(nums)
            if x >= k and y >= k:
                break
            heappush(nums, min(x, y) * 2 + max(x, y))
            ops += 1

        return ops
