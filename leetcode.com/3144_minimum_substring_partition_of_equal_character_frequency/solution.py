class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:

        @cache
        def dfs(i):
            if i >= len(s):
                return 0

            count = Counter()
            m = float('inf')

            _max = 1
            _min = 1

            for j in range(i, len(s)):
                count[s[j]] += 1

                _max = max(_max, count[s[j]])
                _min = min(_min, count[s[j]])

                if _max == _min:
                # if len(set(count.values())) == 1:
                    m = min(m, dfs(j + 1) + 1)

            return m

        return dfs(0)
