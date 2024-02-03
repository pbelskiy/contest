class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        t = 0

        for x1, y1 in points:
            for x2, y2 in points:
                if (x1, y1) == (x2, y2):
                    continue

                # C must be left up of T
                if not (x2 >= x1 and y2 <= y1):
                    continue

                inside = 0
                for x, y in points:
                    if (x, y) == (x1, y1):
                        continue
                    if (x, y) == (x2, y2):
                        continue
                    if x >= x1 and x <= x2 and y >= y2 and y <= y1:
                        inside += 1
                        break

                if inside == 0:
                    t += 1

        return t
