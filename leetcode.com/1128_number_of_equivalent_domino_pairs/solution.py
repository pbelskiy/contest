class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        total = 0
        count = Counter([tuple(sorted(d)) for d in dominoes])

        for k, v in count.items():
            total += math.comb(v, 2)

        return total
