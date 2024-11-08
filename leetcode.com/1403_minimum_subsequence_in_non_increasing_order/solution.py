class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        s = sum(nums)
        a = []
        for i in range(len(nums)):
            if sum(a) > s:
                break
            a.append(nums[i])
            s -= nums[i]

        return a
