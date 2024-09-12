class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:

        def check(a, b):
            if a in b:
                return [b]

            if b in a:
                return [a]

            r = [a + b]

            for i in range(len(b)):
                if a.startswith(b[i:]):
                    r.append(b[:i] + a)

            return r

        def get(a, b):
            return set(check(a, b) + check(b, a))

        def dfs(arr):
            if len(arr) == 1:
                output.add(arr[0])
                return

            for a, b, *rest in permutations(arr):
                for s in get(a, b):
                    dfs([s] + rest)

        output = set()
        dfs([a, b, c])
        return sorted(output, key=lambda s: (len(s), s))[0]
