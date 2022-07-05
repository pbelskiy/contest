class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)

        changed = True
        while changed:
            changed = False

            for i in range(len(ratings) - 1):
                if ratings[i + 1] > ratings[i] and candies[i + 1] <= candies[i]:
                    candies[i + 1] = candies[i] + 1
                    changed = True

            for i in range(len(ratings) - 1, 0, -1):
                if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                    candies[i - 1] = candies[i] + 1
                    changed = True

        return sum(candies)
