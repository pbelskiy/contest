class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        count = Counter()
        timeline = {}
        lead = None
        last = 0

        for p, t in zip(persons, times):
            count[p] += 1

            if count[p] >= last:
                last = count[p]
                lead = p

            timeline[t] = lead

        self.timeline = [(k, v) for k, v in timeline.items()]

    def q(self, t: int) -> int:
        lo, hi = 0, len(self.timeline) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.timeline[mid][0] == t:
                return self.timeline[mid][1]

            if self.timeline[mid][0] > t:
                hi = mid - 1
            else:
                lo = mid + 1

        return self.timeline[hi][1]
