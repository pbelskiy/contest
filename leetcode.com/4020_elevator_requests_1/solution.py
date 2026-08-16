class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        f = 0
        t = 0 

        for n in requests:
            t += abs(f - n)
            f = n

        return t

