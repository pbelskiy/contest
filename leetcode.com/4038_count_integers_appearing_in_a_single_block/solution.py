class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        t = 0
        v = 1 
        d = Counter(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                v += 1
            else:
                if d[nums[i - 1]] == v:
                    t += 1
                v = 1

        if d[nums[-1]] == v:
            t += 1

        return t

