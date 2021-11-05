class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = sum(nums) - sum(set(nums))
        should = sum(range(len(nums) + 1))
        actual = sum(nums) - duplicate

        return [duplicate, abs(should - actual)]
