class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        best = float('-inf')

        for i in range(len(nums)):
            odd = True
            for j in range(i, len(nums) - 1):
                if odd:
                    if nums[j] + 1 != nums[j + 1]:
                        break
                else:
                    if nums[j] - 1 != nums[j + 1]:
                        break

                odd = not odd
                best = max(best, j - i + 2)

        return best if best != float('-inf') else -1
