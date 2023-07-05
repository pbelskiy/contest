class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def solve(i, mi, ma):
            s = tuple(sorted(state))
            if s in d:
                return
            d.add(s)

            if i == len(cookies):
                diff = ma - mi
                if diff <= self.diff:
                    self.diff = diff
                    self.result = max(state)
                return

            for j in range(k):
                state[j] += cookies[i]
                solve(i + 1, min(mi, state[j]), max(ma, state[j]))
                state[j] -= cookies[i]

        self.result = 0
        self.diff = float('inf')

        d = set()
        state = [0]*k
        solve(0, 0, 0)
        return self.result
