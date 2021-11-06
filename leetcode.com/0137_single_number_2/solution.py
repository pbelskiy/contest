class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # N*log(N)*(N/3)
        nums.sort()
        n = len(nums)
        i = 0

        while i < n - 2:
            if nums[i] != nums[i + 2]:
                break

            i += 3
            continue

        return nums[i]
