class Solution:

    def twoSum(self, nums: List[int], curr: int, target: int) -> List[int]:
        deltas = {}

        for i, n in enumerate(nums):
            if i == curr:
                continue

            x = target - n
            # print('x =', x, 'target =', target)
            if x in deltas:
                self.r.add(
                    tuple(sorted([nums[curr], nums[i], nums[deltas[x]]]))
                )

            deltas[n] = i

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.r = set()
        nums.sort()
        # print('\t ->', nums)

        for i, n in enumerate(nums):
            # print(i, n)
            self.twoSum(nums, i, -n)
            # break

        return self.r
