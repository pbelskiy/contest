class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    for m in range(k, n):
                        if not (i < j < k < m):
                            continue

                        if nums[i] + nums[j] + nums[k] == nums[m]:
                            total += 1

        return total
