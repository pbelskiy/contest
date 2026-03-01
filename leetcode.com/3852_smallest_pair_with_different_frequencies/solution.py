class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        keys = sorted(count.keys())

        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if count[keys[i]] == count[keys[j]]:
                    continue

                return [keys[i], keys[j]]

        return [-1, -1]

