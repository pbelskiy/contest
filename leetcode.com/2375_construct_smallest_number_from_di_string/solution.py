class Solution:
    def smallestNumber(self, pattern: str) -> str:

        @cache
        def dfs(s):
            if len(s) == len(pattern) + 1:
                r.append(s)
                return

            curr = pattern[len(s) - 1]

            if curr == 'I':
                for n in range(int(s[-1]), 10):
                    if str(n) not in s:
                        dfs(s + str(n))
            else:
                for n in range(int(s[-1]) - 1, 0, -1):
                    if str(n) not in s:
                        dfs(s + str(n))

        r = []
        for n in range(1, 10):
            dfs(str(n))

        return sorted(r)[0]
