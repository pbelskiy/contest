class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def dfs(s, v, p):
            length = len(s)

            for i in range(p, len(arr)):
                if set(s) & set(arr[i]) or i in v:
                    continue

                nv = v.copy(); nv.add(i)
                length = max(length, dfs(s + arr[i], nv, i))

            return length

        arr = list(filter(lambda a: len(set(a)) == len(a), arr))
        return dfs('', set(), 0)
