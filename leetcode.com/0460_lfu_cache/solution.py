from collections import defaultdict


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.timer = 0
        self.v = {}
        self.f = defaultdict(int)
        self.t = defaultdict(int)

    def _invalidate(self):
        # by frequency
        f_candidates = []

        for k, v in sorted(self.f.items(), key=lambda item: item[1]):
            if f_candidates and v > self.f[f_candidates[0]]:
                break
            f_candidates.append(k)

        if len(f_candidates) == 1:
            self.v.pop(f_candidates[0])
            self.f.pop(f_candidates[0])
            self.t.pop(f_candidates[0])
            return

        # by timer
        t_candidates = {c: self.t[c] for c in f_candidates}
        k, _ = sorted(t_candidates.items(), key=lambda item: item[1], reverse=False)[0]

        self.v.pop(k, None)
        self.f.pop(k, None)
        self.t.pop(k, None)

    def get(self, key: int) -> int:
        value = self.v.get(key)
        if value is None:
            return -1

        self.f[key] += 1
        self.t[key] = self.timer
        self.timer += 1
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.v:
            self.v[key] = value
            self.f[key] += 1
            self.t[key] = self.timer
            self.timer += 1
            return

        if len(self.v) == self.capacity:
            self._invalidate()

        self.v[key] = value
        self.f[key] += 1
        self.t[key] = self.timer
        self.timer += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
