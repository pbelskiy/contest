class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        beauty = Counter(s)
        result = Counter()
        total = 0

        for comb in combinations(set(s), k):
            mul = 1
            for ch in comb:
                mul *= beauty[ch]

            result[sum(beauty[ch] for ch in comb)] += mul

        if not result:
            return 0

        max_beauty = max(result.keys())
        return result[max_beauty] % (10**9 + 7)
