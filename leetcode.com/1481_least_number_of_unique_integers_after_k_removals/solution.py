class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        count = Counter(arr)
        deleted = 0

        for n, t in reversed(count.most_common()):
            if k < t:
                break

            k -= t
            deleted += 1

        return len(count) - deleted
