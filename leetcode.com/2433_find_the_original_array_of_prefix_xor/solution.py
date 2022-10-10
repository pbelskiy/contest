class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        a = [None]*len(pref)
        a[0] = pref[0]

        for i in range(1, len(pref)):
            a[i] = pref[i] ^ pref[i - 1]

        return a
