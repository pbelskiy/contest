from sortedcontainers import SortedSet


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d = defaultdict(SortedSet)
        self.b = {}
        self.r = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.d[c].add((-r, f))
            self.b[f] = c
            self.r[f] = -r

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.b[food]
        self.d[c].discard((self.r[food], food))
        self.d[c].add((-newRating, food))
        self.r[food] = -newRating

    def highestRated(self, cuisine: str) -> str:
        return self.d[cuisine][0][1]
