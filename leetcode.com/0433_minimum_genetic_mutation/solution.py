class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        @cache
        def is_get_diff(s1, s2):
            diff = 0

            for ch1, ch2 in zip(s1, s2):
                if ch1 != ch2:
                    diff += 1

                if diff > 1:
                    return False

            return True

        q = deque([(start, 0)])
        v = set()

        while q:
            a, s = q.popleft()
            if a == end:
                return s

            for b in bank:
                if (a, b) in v:
                    continue
                if is_get_diff(a, b):
                    q.append((b, s + 1))
                    v.add((a, b))

        return -1
