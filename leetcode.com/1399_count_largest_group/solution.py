class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(list)

        for i in range(1, n + 1):
            s = (sum(int(j) for j in str(i)))
            d[s].append(i)

        m = len(max(d.values(), key=len))
        return len(list(filter(lambda v: len(v) == m, d.values())))
