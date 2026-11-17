class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        t = 0

        for i in range(len(nums)):
            m = r = nums[i]
            for j in range(i, len(nums)):
                m = min(m, nums[j])
                r &= nums[j]
                if m == r:
                    t += 1
            
        return t

