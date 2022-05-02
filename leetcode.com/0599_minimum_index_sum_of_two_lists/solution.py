class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        rank = collections.defaultdict(list)
        for val in (set(list1) & set(list2)):
            rank[list1.index(val) + list2.index(val)].append(val)

        return rank[min(rank)]
