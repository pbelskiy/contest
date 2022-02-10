class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [t[0] for t in collections.Counter(nums).most_common(k)]
