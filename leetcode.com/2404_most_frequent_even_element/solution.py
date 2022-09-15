class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(filter(lambda n: n % 2 == 0, nums)).most_common()
        if not count:
            return -1

        return sorted([v for v, c in count if c == count[0][1]])[0]
