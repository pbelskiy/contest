class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = nums[:k]

        for i in range(k, len(nums)):
            m = min(res)

            if nums[i] > m:
                res.remove(m)
                res.append(nums[i])

        return res
