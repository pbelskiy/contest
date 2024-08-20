class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        nums = list(range(n))

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if categoryHandler.haveSameCategory(nums[i], nums[j]):
                    nums[j] = nums[i]

        return len(set(nums))
