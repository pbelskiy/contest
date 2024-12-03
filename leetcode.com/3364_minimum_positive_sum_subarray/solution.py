class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        m = float('inf')
        for i in range(len(nums) - l + 1):
            for j in range(i + l, i + r + 1):
                s = sum(nums[i:j])
                # print(s, nums[i:j])
                if s > 0:
                    m = min(m, s)

        return -1 if m == float('inf') else m
