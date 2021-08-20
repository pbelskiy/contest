class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        if n == 1:
            return True

        count = collections.Counter()

        for w in words:
            count.update(collections.Counter(w))

        for _, v in count.items():
            if v < n or v % n != 0:
                return False

        return True
