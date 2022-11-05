class Solution:
    def oddString(self, words: List[str]) -> str:
        count = defaultdict(list)

        for word in words:
            d = []
            for i in range(len(word) - 1):
                d.append(ord(word[i + 1]) - ord(word[i]))

            count[tuple(d)].append(word)

        for value in count.values():
            if len(value) == 1:
                return value[0]
