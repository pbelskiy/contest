class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        a = []

        for i in range(len(groupSizes)):
            size = groupSizes[i]
            if len(d[size]) == size:
                a.append(d[size])
                d[size] = []

            d[size].append(i)

        return a + list(d.values())
