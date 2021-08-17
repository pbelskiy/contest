class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        p = collections.Counter([ch for ch in licensePlate.lower() if ch.isalpha()])
        candidates = []

        for w in words:
            wc = collections.Counter(w)
            for k, v in p.items():
                if wc[k] < v:
                    break
            else:
                candidates.append(w)

        return min(candidates, key=len)
