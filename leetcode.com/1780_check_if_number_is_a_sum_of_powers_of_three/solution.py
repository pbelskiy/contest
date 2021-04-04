import itertools
import math

class Solution:
    # [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969]
    def checkPowersOfThree(self, n: int) -> bool:
        vals = [3**n for n in range(15)]

        edge = int(math.log(n, 3))
        if edge == n:
            return True

        sl = vals[:edge + 1]
        for limit in range(edge + 1, 0, -1):
            for nums in itertools.combinations(sl, limit):
                if sum(nums) == n:
                    return True

        return False
