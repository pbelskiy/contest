class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        a = sum(nums) / len(nums)
        a1 = math.ceil(a)
        a2 = math.floor(a)
        a3 = nums[len(nums) // 2]

        t1 = 0
        t2 = 0
        t3 = 0

        for n in nums:
            t1 += abs(n - a1)
            t2 += abs(n - a2)
            t3 += abs(n - a3)

        return min(t1, t2, t3)
