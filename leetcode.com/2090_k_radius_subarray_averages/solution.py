class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        a = [-1] * len(nums)
        l, r = 0, k*2 + 1
        s = sum(nums[l:r])

        for i in range(k, len(nums) - k):
            a[i] = int(s / (k*2 + 1))
            if r >= len(nums):
                break
            s -= nums[l]
            s += nums[r]
            l += 1
            r += 1

        return a
