class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        count = defaultdict(int)
        for ch in s:
            count[ch] += 1

        a = list(s)
        m = max(count.values())
        t = set()

        for k, v in count.items():
            if v == m:
                t.add(k)

        # remove extra chars for save relative positions
        for i in range(len(a)):
            if a[i] not in t:
                a[i] = '_'
                continue

            if count[a[i]] > 1:
                count[a[i]] -= 1
                a[i] = '_'

        return ''.join(filter(lambda ch: ch != '_', a))
