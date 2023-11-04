class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(
            max(left, default=0),
            max((n - v for v in right), default=0),
        )
