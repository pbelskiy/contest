class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # decrease high range, skip ranges because & operation property
        while right > left:
            right = right & (right - 1)

        return right
