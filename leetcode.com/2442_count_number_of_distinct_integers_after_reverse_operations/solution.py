class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums.append(int(str(nums[i])[::-1]))

        return len(set(nums))
