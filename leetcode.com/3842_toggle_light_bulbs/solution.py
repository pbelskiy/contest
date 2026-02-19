class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        s = set()

        for b in bulbs:
            if b in s:
                s.remove(b)
            else:
                s.add(b)

        return sorted(s)

