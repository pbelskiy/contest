class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        if a + b <= c or a + c <= b or b + c <= a:
            return "none"

        if len(set(nums)) == 1:
            return "equilateral"

        if len(set(nums)) == 2:
            return "isosceles"

        if len(set(nums)) == 3:
            return "scalene"

