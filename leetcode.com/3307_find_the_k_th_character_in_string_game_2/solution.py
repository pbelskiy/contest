"""
Backward simulation, each step do operation from end to begin.

TC(N)
SC(N)
"""
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        def solve(t, k, i):
            if t == 1:
                return 0

            x = 0
            if k > t // 2:
                x = operations[i]
                k -= t // 2

            return solve(t // 2, k, i - 1) + x

        t = solve(2**len(operations), k, len(operations) - 1)
        return chr(ord('a') + (t % 26))

