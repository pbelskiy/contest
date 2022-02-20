class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = num // 3
        v = [x - 1, x, x + 1]

        if sum(v) != num:
            return []

        return v
