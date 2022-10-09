class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        time = defaultdict(int)
        prev = 0

        for i, t in logs:
            time[i] = max(time[i], t - prev)
            prev = t

        return sorted(time.items(), key=lambda t: (t[1], -t[0]))[-1][0]
