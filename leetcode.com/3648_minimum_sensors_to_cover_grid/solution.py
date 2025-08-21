class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        d = k*2 + 1  # diameter of `tile`
        h = math.ceil(n / d)  # how many tiles need to cover horizontal
        w = math.ceil(m / d)  # how many vertices
        return h*w

