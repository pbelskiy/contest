class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        a1, a2 = list(s1), list(s2)
        set1, set2 = set(), set()

        set1.add(''.join([a1[0], a1[1], a1[2], a1[3]]))
        set1.add(''.join([a1[2], a1[1], a1[0], a1[3]]))
        set1.add(''.join([a1[0], a1[3], a1[2], a1[1]]))

        set2.add(''.join([a2[0], a2[1], a2[2], a2[3]]))
        set2.add(''.join([a2[2], a2[1], a2[0], a2[3]]))
        set2.add(''.join([a2[0], a2[3], a2[2], a2[1]]))

        return set1 & set2
