class Solution:
    def minimumPushes(self, word: str) -> int:
        t = 0
        for i in range(len(Counter(word).most_common())):
            t += 1 + (i // 8)

        return t
