class Solution:
    def countTime(self, time: str) -> int:

        def solve(t):
            if '?' not in t:
                try:
                    datetime.datetime.strptime(t, '%H:%M')
                except Exception:
                    ...
                else:
                    valid.add(t)
                return

            for i in range(len(t)):
                if t[i] == '?':
                    for n in range(10):
                        solve(t[:i] + str(n) + t[i+1:])

        valid = set()
        solve(time)
        return len(valid)
