class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def is_possible(c1, c2):
            c3 = Counter(c1)
            c3.subtract(c2)
            return c3, min(c3.values()) >= 0

        def dfs(i, c):
            if i == len(data):
                return 0

            nc, possible = is_possible(c, data[i][1])

            if possible:
                a = data[i][0] + dfs(i + 1, nc)
            else:
                a = 0

            return max(a, dfs(i + 1, c))

        data = []

        for word in words:
            w_count = Counter(word)

            nc, possible = is_possible(Counter(letters), w_count)

            if possible:
                w_score = sum([score[ord(ch) - ord('a')] for ch in word])
            else:
                w_score = 0

            data.append((w_score, w_count))

        return dfs(0, Counter(letters))
