"""
Use stack, and greedy solve the task

TC: O(NlgN)
SC: O(N)
"""
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []

        for n in nums:
            s.append(n)
            while len(s) > 1 and math.gcd(s[-1], s[-2]) > 1:
                s.append(math.lcm(s.pop(), s.pop()))

        return s

