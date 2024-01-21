class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)

        t = 0
        n = 0
        for k, v in count.most_common():
            t += (1 + (n // 8)) * v
            n += 1

        return t
