class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)

        try:
            return not ((cnt1 - cnt2).most_common()[0][1] > 3 or (cnt2 - cnt1).most_common()[0][1] > 3)
        except IndexError:
            return True
