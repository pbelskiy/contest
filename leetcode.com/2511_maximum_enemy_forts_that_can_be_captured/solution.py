class Solution:
    def captureForts(self, forts: List[int]) -> int:

        def get(i):
            a = 0
            for j in range(i + 1, len(forts)):
                if forts[j] == 0:
                    a += 1
                elif forts[j] == 1:
                    a = 0
                    break
                elif forts[j] == -1:
                    break
            else:
                a = 0

            b = 0
            for j in range(i - 1, -1, -1):
                if forts[j] == 0:
                    b += 1
                elif forts[j] == 1:
                    b = 0
                    break
                elif forts[j] == -1:
                    break
            else:
                b = 0

            return max(a, b)

        m = 0
        for i in range(len(forts)):
            if forts[i] == 1:
                m = max(m, get(i))

        return m
