class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        def solve(s):
            state = [0]*n
            used = [0]*n
            total = 0

            for i in range(len(requests)):
                if s & (1 << i):
                    state[requests[i][0]] -= 1
                    state[requests[i][1]] += 1

                    used[requests[i][0]] = 1
                    used[requests[i][1]] = 1

                    total += 1

            for i in range(n):
                if used[i] == 1 and state[i] != 0:
                    return 0

            return total

        best = 0
        for i in range(2**len(requests)):
            best = max(best, solve(i))

        return best
