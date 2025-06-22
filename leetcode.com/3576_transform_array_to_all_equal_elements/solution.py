class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:

        def solve(nums, k):
            for j in range(len(nums) - 1):
                if nums[j] == -1:
                    nums[j] = 1 
                    nums[j + 1] = 1 if nums[j + 1] == -1 else -1

                    k -= 1
                    if k == 0:
                        break

            return len(set(nums)) == 1

        return solve(nums[:], k) or solve([-n for n in nums], k)

