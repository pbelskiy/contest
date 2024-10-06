class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        a, b, c = bin(nums[0])[2:], \
                  bin(nums[1])[2:], \
                  bin(nums[2])[2:]

        return max(
            int(a + b + c, 2),
            int(a + c + b, 2),
            int(b + a + c, 2),
            int(b + c + a, 2),
            int(c + a + b, 2),
            int(c + b + a, 2),
        )
