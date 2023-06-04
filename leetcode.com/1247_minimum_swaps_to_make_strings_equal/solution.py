class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        count = Counter(s1 + s2)
        if count['x'] % 2 == 1 or count['y'] % 2 == 1:
            return -1

        a1, a2, ops = list(s1), list(s2), 0

        while a1 != a2:
            # strip matches
            for i in range(len(a1)):
                if a1[i] == a2[i]:
                    a1[i], a2[i] = None, None

            a1 = [v for v in a1 if v is not None]
            a2 = [v for v in a2 if v is not None]

            # swap unequal
            for i in range(1, len(a2)):
                if a2[0] == a2[i]:
                    a1[0], a2[i] = a2[i], a1[0]
                    break
            else:
                a1[0] = a2[0]

            ops += 1

        return ops
