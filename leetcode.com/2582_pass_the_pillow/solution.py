class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        q, r = divmod(time, n - 1)
        if q % 2 == 0:      # even cycles
            return 1 + r    # return position
        return n - r        # odd cycles, position from end
