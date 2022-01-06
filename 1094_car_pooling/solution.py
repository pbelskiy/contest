class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        s, p = 0, []

        for n, b, e in trips:
            p.append((b, +n))
            p.append((e, -n))

        p.sort()

        for i, n in p:
            s += n

            if s > capacity:
                return False

        return True
