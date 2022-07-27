class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        n = Counter(ranks).most_common()[0][1]

        if n >= 3:
            return "Three of a Kind"

        if n == 2:
            return "Pair"

        return "High Card"
