class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words.sort()

        longest = 0
        sets = [set(w) for w in words]

        for i1, w1 in enumerate(words):
            for i2, w2 in enumerate(words):
                if i1 == i2:
                    continue

                if not (sets[i1] & sets[i2]):
                    longest = max(longest, len(w1) * len(w2))

        return longest
