class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        @cache
        def get_diff(s):
            t = 0
            n = len(s) // 2

            for a, b in zip(s[:n], s[n:][::-1]):
                t += a != b

            return t

        @cache
        def is_semipalindrome(a, b):
            l = b - a
            m = float('inf')

            for d in range(1, l // 2 + 1):
                if l % d != 0:
                    continue

                t = 0
                x = 0

                for g in range(d):
                    n = get_diff(s[a + g:b:d])
                    if n == 0:
                        t += 1
                    else:
                        x += n

                if d == t:
                    return 0

                m = min(m, x)

            return m

        @cache
        def dfs(i, k):
            if k == 0:
                return is_semipalindrome(i, len(s))

            m = float('inf')

            for j in range(i + 2, len(s) - 2*k + 1):
                m = min(m, dfs(j, k - 1) + is_semipalindrome(i, j))

            return m

        return dfs(0, k - 1)

