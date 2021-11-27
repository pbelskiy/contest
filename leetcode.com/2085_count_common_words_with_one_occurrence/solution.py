class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = collections.Counter(words1)
        cnt2 = collections.Counter(words2)

        total = 0

        for k, v in cnt1.items():
            if v == 1 and k in cnt2 and cnt2[k] == 1:
                total += 1

        return total
