class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = {b: a + 1 for a, b in zip(range(len(score)), sorted(score, reverse=True))}
        res = []

        for s in score:
            v = str(ranks[s])

            if v == '1':
                v = 'Gold Medal'
            elif v == '2':
                v = 'Silver Medal'
            elif v == '3':
                v = 'Bronze Medal'

            res.append(v)

        return res
